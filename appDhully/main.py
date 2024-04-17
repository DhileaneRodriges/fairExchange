import os
import sys
from appDhully.alice.Configurations import ConfigsAlice
from appDhully.service.EncryptationProcessService import EncryptationProcessService
from appDhully.bob.Configurations import ConfigsBob
from appDhully.service.ExchangeEncyptedFileService import ExchangeEncryptedFile

def main():
    options = {
        1: start_encryption_process,
        2: start_exchange_process,
        3: open_notepad,
        0: exit_program
    }

    while True:
        print_options()
        option = int(input("Enter an option: "))
        if option in options:
            options[option]()
        else:
            print("Invalid option. Please try again.")

def start_encryption_process():
    confAlice, confBob = create_configs()
    EncryptationProcessService().startProcess(confAlice)
    EncryptationProcessService().startProcess(confBob)

def start_exchange_process():
    aliceConf, bobConf = create_configs()
    exchangeDocuments = ExchangeEncryptedFile()
    exchangeDocuments.startProcess(bobConf, aliceConf)

def create_configs():
    return ConfigsAlice(), ConfigsBob()
def print_options():
    print("Press 1 to encrypts your document on Attestable.")
    print("Press 2 to exchange documents Encrypted.")
    print("Press 3 Attestable descrypt and validete documents.")
    print("Press 4 Attestable confime veracity in PBB.")
    print("Press 0 to exit of system.")

def open_notepad():
    os.system("start notepad")

def exit_program():
    sys.exit()

if __name__ == '__main__':
    main()