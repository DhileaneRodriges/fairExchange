"""
title           : test_app_request_bobdoc.py 
description     : It communicates with alice's attestable, sends a message
                : and receives Alice's document in  encrypyed format under
                : a symmetric key shared between Alice's attestable and
                : Bob's attestable.  
                : I tested it only on the same LAN (in the computer lab), 
                : not firewall: between server and client.
                :
inspiration     : https://github.com/mikepound/tls-exercises
source          :
                : 
author          : Carlos Molina-Jimenez
                : carlos.molina@cl.cam.ac.uk
                : Computer Lab, University of Cambridge
date            : 11 Sep 2023
version         : 1.0 
                :
usage           : 
notes           :
compile and run :
                : cm770@morello-camb-1: $ py test_app_request_bobdoc.py 
                :      -s localhost 
                :      -p 8290 -f helloAttestable.txt
                : cm770@morello-camb-1: $ py test_app_request_bobdoc.py 
                :
python_version  : Python 3.7.4 (v3.7.4:e09359112e, Jul 8 2019)      
"""

from app_request_bobdoc import  SSLclientfile 


def main():
  import argparse
  parser = argparse.ArgumentParser(description="Bob app acting as a client")
  #parser.add_argument("-s", "--server", help="Host where Bob's attestable runs, default is morello-camb-3.sm.cl.cam.ac.uk", default= "morello-camb-3.sm.cl.cam.ac.uk")
  parser.add_argument("-s", "--server", help="Host where Bob's attestable runs, default is localhost", default= "localhost")
  parser.add_argument("-p", "--port", help="Attestable's port, default is ", default= 8290)
  parser.add_argument("-f", "--file", help="File to send to Bob's attestable , default is helloAttestable.txt", default= "helloAttestable.txt")

  args         = parser.parse_args()
  server       = args.server
  port         = args.port  
  file_to_send = args.file
  
  cli= SSLclientfile()
  cli.sockconnect(server, int(port)) # deft server= "morello-camb-3", port=8290
  cli.send_recv_file(file_to_send)   # 11 Sep 2023: NO file is sent, I need to update 


if __name__ == '__main__':
    main()
