import os
import sys
import time

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
    last_successful_option = 0
    encrypted_files_1 = None
    encrypted_files_2 = None

    while True:
        time.sleep(2)
        print_options()
        option = int(input("Enter an option: "))
        if option in options:
            if option > last_successful_option + 1:
                print(f"----------------------------------------------------------------------------------------------------")
                print(f"You must successfully complete option {last_successful_option + 1} before selecting option {option}.")
                print(f"----------------------------------------------------------------------------------------------------")
            else:
                if option == 1:
                    success, encrypted_files_1, encrypted_files_2= options[option]()
                elif option == 2 and encrypted_files_1 and encrypted_files_2 is not None:
                    success = options[option](encrypted_files_1, encrypted_files_2)
                else:
                    success = options[option]()
                if success:
                    last_successful_option = option
        else:
            print("Invalid option. Please try again.")

def start_encryption_process():
    confAlice, confBob = create_configs()
    successAlice, encrypted_file_Alice  = EncryptationProcessService().startProcess(confAlice)
    successBob, encrypted_file_Bob = EncryptationProcessService().startProcess(confBob)
    return successAlice and successBob, encrypted_file_Alice, encrypted_file_Bob

def start_exchange_process(encrypted_file_Alice, encrypted_file_Bob):
    aliceConf, bobConf = create_configs()
    exchangeDocuments = ExchangeEncryptedFile()
    exchangeDocuments.startProcess(bobConf, aliceConf, encrypted_file_Alice, encrypted_file_Bob)

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