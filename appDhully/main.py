import argparse
import os
import time
from module.ServerModule import Module
from alice.utils.settings.ConfigModule import ConfigAliceModule
from bob.utils.settings.module_setting import ModuleSettings

if __name__ == '__main__':
   while True:
      print("Press 1 to Alice encrypts your document in your Attestable.")
      print("Press 2 to Bob encrypts your document in your Attestable.")
      print("Press 3 Alice and bob send yours documents encrypted.")
      print("Press 0 to exit of system. ")

      print("Enter an option: ")
      x = int(input())

      if x == 1:
         print("1 - Alice start your Attestable")
         settingsModuleAlice = ConfigAliceModule()  # Uma instância da classe ConfigAliceModule atribuída a variável settingsModuleAlice

         # A classe ConfigAliceModule é responsável por configurar ou fornecer configurações específicas para o módulo Alice.

         moduleAlice = Module(settingsModuleAlice)  # Nesta linha, o móduloAlice está sendo instanciado com as configurações fornecidas pela instância de ConfigAliceModule (settingsModuleAlice).

         # A instância do módulo é então executada usando o método run().
         print("start o modulo")
         time.sleep(2)
         print("2- Alice sends a request to Attestable to encrypt document")
         time.sleep(2)
         print("3 - Response Attestable with document encrypted")
         time.sleep(2)
         print("------Finish process encriptacion-----")
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