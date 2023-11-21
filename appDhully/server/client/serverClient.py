
import socket
import ssl
from pathlib import Path

# five new lines
import os

from appDhully.server.files2sockets import recv_store_file

class SSLclientfile():

 def __init__(self, configClient):

     config = configClient.configServers
     self.clientname = config.client_name
     self.server = config.server
     self.port = config.port
     self.headersize = 10
     self.soc = None
     self.conn = None
     print("\n", self.clientname, " wants to run... Its PEM pass phrase is: camb\n")

 def sockconnect(self, ser="localhost", port=8080):
     self.server= ser
     self.port= port

     self.soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

     # Create a standard TCP Socket
     # Create SSL context which holds the parameters for any sessions
     context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
     context.load_verify_locations(CA_CERT)
     context.load_cert_chain(certfile=CLIENT_CERT_CHAIN, keyfile=CLIENT_KEY)


     # We can wrap in an SSL context first, then connect
     self.conn= context.wrap_socket(self.soc, server_hostname="attestable alice CAMB")

     ## OK 27Jul2023 return(self.conn.connect((ser, port)))
     return(self.conn.connect((self.server, self.port)))
     # this version does not use this return value



 def send_recv_file(self, fname): 
     conn=self.conn
     try:
        # This method uses the already connected conn socket 

        print("Negotiated session using cipher suite: {0}\n".format(conn.cipher()[0]))

        """ 
        11 sep 2023
        # experimenting with simon.txt file stored on current subdir
        #filename= FILE_NAME 
        filename= fname 
        filesize= os.path.getsize(filename)

        # In python sockets send and receive strings. Send a string 
        conn.send(f"{filename}{SEPARATOR}{filesize}".encode())


        ########## client will send file to server ########
        read_send_file(filename, filesize,  BUFFER_SIZE, conn)
        11 sep 2023
        """ 

        print("cli-request_file.py: before send")
        conn.send(b"Send me your encrypted doc!\n") 
        print("cli-request_file.py: after send")
         

        #####  client will receive file from server #####
        print("cli_file_flie.py now waiting from string from ser_file_file.py")
        received= conn.recv(BUFFER_SIZE).decode()
        filename, filesize= received.split(SEPARATOR)
        # remove filename path if any
        filename= os.path.basename(filename)
        filename= RECV_FILE_NAME_PREFIX + filename
        filesize= int(filesize)
        # start receiving the file from the socket
        # and writing to the file stream
        recv_store_file(filename, filesize, BUFFER_SIZE, conn)
        print("cli_file_flie.py has received file from ser_file_file.py")

     finally:
        if self.conn is not None:
           self.conn.close()




if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description="Alice's app contacys Alice's attestable and requests Alice's doc")
    parser.add_argument("-s", "--server", help="Server, default is localhost", default= "localhost")
    parser.add_argument("-p", "--port", help="Alice's attestable port, default is ", default=8290)
    parser.add_argument("f", "--file", help="File to send to Alice attestable", default="helloAttestable.txt")

    args      = parser.parse_args()
    server    = args.server
    port      = args.port
    file      = args.file  # carlos (11 sep 2023) NOT in use 

    c=SSLclientfile()
    c.sockconnect(server, port) # deft server= "localhost", port=8290
    c.send_recv_file(file)      # 11 sep 2023: NO file is sent, I need to update
