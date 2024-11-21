import hashlib
import socket
import threading
import time

from appDhully.PBB.client import start_client
from appDhully.PBB.main_pbb import start_server

class PBBService():
    def __int__(self):
        pass

    def startProcess(self, list_of_options):
        print(f"-----------------------------------------------------------------------------------------")
        print(f"------Begin PBB process -----")
        sizeOptions = len(list_of_options)-1
        i = 0
        for person in list_of_options:

            if(i==0):
                server_thread = threading.Thread(target=self.startPbbServer, name="pbb_server")
                server_thread.start()
                time.sleep(5)

            if(i==sizeOptions):
                self.upClienteToSendSignalToPBB(person['cliente_name'], person["pass"], person['value'])
                break
            else:
                thread = threading.Thread(target=self.upClienteToSendSignalToPBB, name="client_pbb",
                                                args=(person['cliente_name'], person['pass'], person['value']))
                thread.start()
                time.sleep(2)

            i += 1


        print(f"-----------------------------------------------------------------------------------------")
        print(f"------finish PBB process-----")

    def startPbbServer(self):

        start_server()

    def upClienteToSendSignalToPBB(self, clientName, key, signal):
        start_client(clientName, key, signal)
