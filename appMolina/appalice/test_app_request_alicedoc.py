from app_request_alicedoc import  SSLclientfile


def main():
  import argparse
  parser = argparse.ArgumentParser(description="Alice app acting as a client")
  #parser.add_argument("-s", "--server", help="Host where Alice's attestable runs, default is morello-camb-3.sm.cl.cam.ac.uk", default= "morello-camb-3.sm.cl.cam.ac.uk")
  parser.add_argument("-s", "--server", help="Host where Alice's attestable runs, default is localhost", default= "localhost")
  parser.add_argument("-p", "--port", help="Attestable's port, default is ", default= 8080)
  parser.add_argument("-f", "--file", help="File to send to Alice's attestable , default is helloAttestable.txt", default= "helloAttestable.txt")

  args         = parser.parse_args()
  server       = args.server
  port         = args.port  
  file_to_send = args.file
  
  cli= SSLclientfile()
  cli.sockconnect(server, int(port)) # deft server= "morello-camb-3", port=8290
  cli.send_recv_file(file_to_send)   # 11 Sep 2023: NO file is sent, I need to update 


if __name__ == '__main__':
    main()
