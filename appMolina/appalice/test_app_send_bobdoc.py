#from cli_send_file import  SSLclientfile
from app_send_alicedoc import  SSLclientfile 

def main():
  import argparse
  parser = argparse.ArgumentParser(description="Alice app acting as a client")
  parser.add_argument("-s", "--server", help="Host where Alice's attestablei run, default is localhost", default= "localhost")
  parser.add_argument("-p", "--port", help="Server port, default is ", default= 8290)
  parser.add_argument("-f", "--file", help="File to send to server, default is helloServer.txt", default= "helloServer.txt")

  args         = parser.parse_args()
  server       = args.server
  port         = args.port  
  file_to_send = args.file
  
  cli= SSLclientfile()
  cli.sockconnect(server, int(port)) # deft server= "morello-camb-3", port=8290
  cli.send_recv_file(file_to_send) 


if __name__ == '__main__':
    main()
