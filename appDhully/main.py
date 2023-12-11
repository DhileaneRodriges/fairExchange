import os
import time
from appDhully.server.module.serverModule import Module
from appDhully.server.client.serverClient import SSLClientFile
from appDhully.alice.Configurations import ConfigsAlice


def main():
   while True:
      print_options()
      option = int(input("Enter an option: "))

      if option == 1:
         process_encryption("Alice", ConfigsAlice())
      elif option == 2:
         process_encryption("Bob", None)  # Add Bob configurations
      elif option == 3:
         open_notepad()
      elif option == 0:
         exit_program()


def print_options():
   print("Press 1 to Alice encrypts your document in your Attestable.")
   print("Press 2 to Bob encrypts your document in your Attestable.")
   print("Press 3 Alice and bob send yours documents encrypted.")
   print("Press 0 to exit of system.")


def process_encryption(name, configurations):
   print(f"------Begin process encryption {name}'s document-----")

   if configurations:
      module = Module(configurations)
      print(f" --> 1 - {name} start your Attestable")
      time.sleep(5)

      ssl_client_file = SSLClientFile(configurations)
      ssl_client_file.sock_connect()
      ssl_client_file.send_recv_file(configurations.configServers.config_client.cliente_file)
      print(f" --> 2 - {name} sends a request to Attestable to encrypt document")

      time.sleep(5)
      print(" --> 3 - Response Attestable with document encrypted")
      time.sleep(5)

   print(f"------Finish process encryption {name}'s document-----")
   time.sleep(6)


def open_notepad():
   os.system("start notepad")


def exit_program():
   exit()


if __name__ == '__main__':
   main()