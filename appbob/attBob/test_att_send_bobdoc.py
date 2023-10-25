"""
title           : test_att_send_bobdoc.py 
description     : It is a server running in Bob's attestable that
                : upon request from Bob's application, sends
                : Bob's encrypted document under a symmetric key
                : shared between Bob's attestable and Alice's
                : attestable.
                : It tests the the SSLserverfile class. 
                : By defaut it assumes that Bob's application and
                : Bob's attestable run on the same computer. 
                : I tested it only on the same LAN (in the computer lab)
                : not firewall between server and client.
                : 
inspiration     : https://github.com/mikepound/tls-exercises
source          :
                : 
author          : Carlos Molina-Jimenez
                : carlos.molina@cl.cam.ac.uk
                : Computer Lab, University of Cambridge
date            : 12 Aug 2023
version         : 1.0 
                :
usage           : 
notes           : I have tested only with morello-camb-3.sm.cl.cam.ac.uk 
                : and port 8290
                : It assumes the existence of helloClient.txt 
                : in current folder. 
                :
compile and run : cm770@morello-camb-3: $ python3 test_att_send_bobdoc.py 
                :    -s localhost 
                :    -p 9290 -f bobdoc_encrypted.txt
                :
                : Alternatively
                : cm770@morello-camb-3: $ python3 test_att_send_bobdoc.py 
                :
python_version  : Python 3.7.4 (v3.7.4:e09359112e, Jul 8 2019)      
                :
"""

#from ser_send_file import  SSLserverfile 
from att_send_bobdoc import  SSLserverfile 

def main():
  import argparse
  parser = argparse.ArgumentParser(description="Bob's attestable")
  parser.add_argument("-s", "--server_name", help="localhost", default="localhost")
  parser.add_argument("-p", "--port_number", help="port used by server", default="8290")
  parser.add_argument("-f", "--file_to_send", help="file to send to the application", default="bobdoc_encrypted.txt")
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
