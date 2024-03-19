import os
import time
from appDhully.alice.Configurations import ConfigsAlice
from appDhully.service.EncryptationProcessService import EncryptationProcessService
from appDhully.bob.Configurations import ConfigsBob
from appDhully.service.ExchangeEncyptedFileService import ExchangeEncryptedFile


def main():
    while True:
        print_options()
        option = int(input("Enter an option: "))

        if option == 1:
            confAlice = ConfigsAlice()
            confBob = ConfigsBob()

            EncryptationProcessService().startProcess(confAlice)
            EncryptationProcessService().startProcess(confBob)
        elif option == 2:

            aliceConf = ConfigsAlice()
            bobConf = ConfigsBob()

            exchangeDocuments = ExchangeEncryptedFile()
            exchangeDocuments.startProcess(bobConf, aliceConf)

        elif option == 3:
            open_notepad()
        elif option == 0:
            exit_program()

def print_options():
    print("Press 1 to encrypts your document on Attestable.")
    print("Press 2 to exchange documents Encrypted.")
    print("Press 3 Attestable descrypt and validete documents.")
    print("Press 4 Attestable confime veracity in PBB.")
    print("Press 0 to exit of system.")


def open_notepad():
    os.system("start notepad")


def exit_program():
    exit()


if __name__ == '__main__':
    main()
