"""
notes           : I have tested only with localhost
                : and port 8290
                : It assumes the existence of helloClient.txt 
                : in current folder. 

"""

from config_recv_alicedoc import SSLserverfile

def main():
  import argparse
  parser = argparse.ArgumentParser(description="Alice's server running inside Alice's attestable")
  parser.add_argument("-s", "--server_name", help="localhost", default="localhost")
  parser.add_argument("-p", "--port_number", help="port used by server", default="8081")
  parser.add_argument("-f", "--file_to_send", help="file to send to client", default="alicedoc_encrypted.txt")
  args         = parser.parse_args()
  server_name  = args.server_name 
  port_number  = args.port_number
  file_to_send = args.file_to_send
  
  server = SSLserverfile()
  server.start_server(server_name, int(port_number), file_to_send)
                     # server_name: fully qualified hostname of computer
                     # hosting this server
                     # file_to_send: name of the file that server sends to 
                     # client as response.
                     

if __name__ == '__main__':
    main()
