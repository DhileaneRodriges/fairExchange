import argparse
import os
import time
from module.ServerModule import Module
from alice.utils.settings.ConfigModule import ConfigAliceModule
from bob.utils.settings.module_setting import ModuleSettings

if __name__ == '__main__':
   while True:
      print("Press 1 to Alice encript your document in your module.")
      print("Press 2 to Bob encript your document in your module.")
      print("Press 3 Alice and bob send yours documents encripted.")
      print("Press 0 to exit of sistem. ")

      x = int(input())
      if x == 1:
         print("1 - Alice start your module")
         settingsModuleAlice = ConfigAliceModule()
         moduleAlice = Module(settingsModuleAlice).run()


         time.sleep(2)
         print("2- Alice send a request to module to encript document")
         time.sleep(2)
         print("3 - Resposne module with document encripted")
         time.sleep(2)
         print("------Fnish process encripty-----")
         time.sleep(3)
      elif 2 == x:
         print("module bob init and listen requeste")
         time.sleep(2)
         print("Bob send a request to module to encript document")
         time.sleep(2)
         print("Resposne module with document encripted")
         time.sleep(2)
         print("Fnish process encripty")
      elif x == 3:
         os.system("start notepad")
      elif x == 0:
         exit();