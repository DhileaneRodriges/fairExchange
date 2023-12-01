import os
import time
from appDhully.server.module.serverModule import Module
from appDhully.server.client.serverClient import SSLclientfile
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
      time.sleep(2)

      ssl_client_file = SSLclientfile(configurations)
      ssl_client_file.sockconnect()
      ssl_client_file.send_recv_file()
      print(f" --> 2 - {name} sends a request to Attestable to encrypt document")

      time.sleep(2)
      print(" --> 3 - Response Attestable with document encrypted")
      time.sleep(2)

   print(f"------Finish process encryption {name}'s document-----")
   time.sleep(3)


def open_notepad():
   os.system("start notepad")


def exit_program():
   exit()


if __name__ == '__main__':
   main()

if __name__ == '__main__':
   while True:
      print("Press 1 to Alice encrypts your document in your Attestable.")
      print("Press 2 to Bob encrypts your document in your Attestable.")
      print("Press 3 Alice and bob send yours documents encrypted.")
      print("Press 0 to exit of system. ")

      print("Enter an option: ")
      x = int(input())

      if x == 1:
         print("------Begin process encryption Alice`s document-----")
         settingsModuleAlice = ConfigsAlice()

         moduleAlice = Module(settingsModuleAlice)
         print(" --> 1 - Alice start your Attestable")

         time.sleep(2)

         sslclientfile = SSLclientfile(settingsModuleAlice)
         sslclientfile.sockconnect()
         sslclientfile.send_recv_file()
         print(" --> 2 - Alice sends a request to Attestable to encrypt document")

         time.sleep(2)
         print(" --> 3 - Response Attestable with document encrypted")
         time.sleep(2)

         print("------Finish process encryption Alice`s document-----")
         time.sleep(3)
      elif 2 == x:
         print("Attestable bob init and listen requeste")
         time.sleep(2)
         print("Bob sends a request to Attestable to encrypt document")
         time.sleep(2)
         print("Response Attestable with document encrypted")
         time.sleep(2)
         print("Finish process encriptacion")
      elif x == 3:
         os.system("start notepad")
      elif x == 0:
         exit();