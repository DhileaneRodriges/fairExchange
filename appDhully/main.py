import os
import time
from appDhully.server.initServer import Server
from appDhully.client.serverClient import SSLClientFile
from appDhully.alice.Configurations import ConfigsAlice
from appDhully.bob.Configurations import ConfigsBob


def main():
   while True:
      print_options()
      option = int(input("Enter an option: "))

      if option == 1:
         process_encryption( ConfigsAlice())
         process_encryption( ConfigsBob())
      elif option == 2:
         process_encryption("Bob", None)  # Add Bob configurations
      elif option == 3:
         open_notepad()
      elif option == 0:
         exit_program()


def print_options():
   print("Press 1 to encrypts your document on Attestable.")
   print("Press 2 to change documents Encrypted.")
   print("Press 3 Attestable descrypt and validete documents.")
   print("Press 4 Attestable confime veracity in PBB.")
   print("Press 0 to exit of system.")


def process_encryption(configurations):
   print(f"-----------------------------------------------------------------------------------------")
   print(f"------Begin process encryption {configurations.configServers.client_name}'s document-----")

   if configurations:
      module = Server(configurations)
      print(f" --> 1 - {configurations.configServers.client_name} start your Attestable")
      time.sleep(2)

      ssl_client_file = SSLClientFile(configurations)
      ssl_client_file.sock_connect()
      ssl_client_file.send_recv_file(configurations.configServers.config_client.cliente_file)
      ssl_client_file.conn.close()
      time.sleep(2)

   print(f"------Finish process encryption {configurations.configServers.client_name}'s document-----")
   time.sleep(6)


def open_notepad():
   os.system("start notepad")


def exit_program():
   exit()


if __name__ == '__main__':
   main()