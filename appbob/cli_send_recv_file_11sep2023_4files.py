"""
title           : cli_send_recv_file.py 
description     : Is a client that establishes a secure chan over ssl
                : with a server if mutual authentication succeeds.
                :
                : I created the self-signed certificates following the steps
                : https://github.com/mikepound/tls-exercises/tree/master/ca
                :
                : 1) It requests aconnection 
                : 2) If accepted, it sends a file.
                : 3) It expects another file as a response from server.
                : I tested it with plain txt, jpeg and encrypted
                : files under
                : encrypt
                : $ openssl aes-256-cbc -e -salt -pbkdf2 -iter 10000 -in 
                :   cat.jpg -out cat_encrypted.dat
                : decrypt
                : $ openssl aes-256-cbc -d -salt -pbkdf2 -iter 10000 -in
                : cat_encrypted.dat -out cat_decrypted.jpg
                :
                : 
source          : https://github.com/mikepound/tls-exercises
                : 
author          : Carlos Molina Jimenez
date            : 3 Sep 2023
version         : __
usage           : 
notes           : I have tested only with "localhost" (i.e 127.0.0.1)
                : and port 8282
compile and run : % python3 cli_send_recv_file.py file_to_send 
                : Alternatively the main class of this module 
                : (SSLclientfile) can be tested by the testing
                : program test_SSLclientfile
                : 
                : % test_SSLclientfile.py # sends helloServer.txt by default 
                :
python_version  : Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:36:03     
                :
"""
import socket
import ssl
from pathlib import Path

# five new lines
import tqdm
import os
import argparse

from files2sockets import read_send_file, recv_store_file

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 1024 * 4 #4KB
HEADERSIZE= 10

#RECV_FILE_NAME_PREFIX= "fuchi_fromSer_"
RECV_FILE_NAME_PREFIX= ""


#LOCAL_HOST = 'localhost'
#LOCAL_HOST = "morello-camb-3.sm.cl.cam.ac.uk" 
LOCAL_HOST = "localhost"
LOCAL_PORT = 8290
RESOURCE_DIRECTORY = Path(__file__).resolve().parent.parent / 'certskeys' / 'client'
CLIENT_CERT_CHAIN = RESOURCE_DIRECTORY / 'aliceClient.intermediate.chain.pem'
CLIENT_KEY = RESOURCE_DIRECTORY / 'aliceClient.key.pem'
CA_CERT = RESOURCE_DIRECTORY / 'rootca.cert.pem'






class SSLclientfile():

 def __init__(self, clientname= "client", server=LOCAL_HOST, port=LOCAL_PORT):
  self.clientname= clientname
  self.server= server 
  self.port= port
  self.headersize= HEADERSIZE 
  self.soc= None
  self.conn= None
  print("\n", self.clientname, " wants to run... Its PEM pass phrase is: camb\n")


 def sockconnect(self, ser="localhost", port=8282):
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


        # experimenting with simon.txt file stored on current subdir
        #filename= FILE_NAME 
        filename= fname 
        filesize= os.path.getsize(filename)

        # In python sockets send and receive strings. Send a string 
        conn.send(f"{filename}{SEPARATOR}{filesize}".encode())


        ########## client will send file to server ########
        read_send_file(filename, filesize,  BUFFER_SIZE, conn)


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

        ##################
        # send alicedoc_encrypted to Bob's app and
        # wait for bobdoc_encrypted from Bob's app
        ##################

        # experimenting with bobdoc_encrypted.txt file stored on current subdir
        #filename= FILE_NAME 
        #filename= fname 
        filename= "bobdoc_encrypted.txt" 
        filesize= os.path.getsize(filename)

        # In python sockets send and receive strings. Send a string 
        conn.send(f"{filename}{SEPARATOR}{filesize}".encode())


        ########## client will send file to server ########
        read_send_file(filename, filesize,  BUFFER_SIZE, conn)




     finally:
        if self.conn is not None:
           self.conn.close()




if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description="Alice's app that sends and receives a files")
    parser.add_argument("-s", "--server", help="Server, default is localhost", default= "localhost")
    parser.add_argument("-p", "--port", help="Server port, default is ", default=8290)
    parser.add_argument("file", help="File name to send")

    args      = parser.parse_args()
    server    = args.server
    port      = args.port
    file_name = args.file 

    c=SSLclientfile()
    c.sockconnect(server, port) # deft server= "localhost", port=8290
    c.send_recv_file(file_name) 
