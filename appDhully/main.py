import os
import time
from appDhully.server.Server import Server
from appDhully.client.Client import ClientSSL
from appDhully.alice.Configurations import ConfigsAlice
from appDhully.bob.Configurations import ConfigsBob

def main():
    while True:
        print_options()
        option = int(input("Enter an option: "))

        if option == 1:
            process_encryption(ConfigsAlice())
            process_encryption(ConfigsBob())
        elif option == 2:
            print(f"-----------------------------------------------------------------------------------------")
            print(f"------Begin process exchange document-----")

            aliceConf = ConfigsAlice()
            bobConf = ConfigsBob()

            upServerToReceivDocEncrypted(bobConf, bobConf.configuration.config_server.intermadiate_server_cert_chain,
                    bobConf.configuration.config_server.intermadiate_server_key,
                    bobConf.configuration.server_name, 8290 )

            upClienteToSendDocumentEncripted(aliceConf, bobConf.configuration.client_name, aliceConf.configuration.config_client.intermadiate_client_cert_chain,
                    aliceConf.configuration.config_client.intermadiate_client_key,
                    bobConf.configuration.server_name, 8290)

            #time.sleep(2)
            #upServerToReceivDocEncrypted(ConfigsBob())
            #upClienteToSendDocumentEncripted(ConfigsAlice())
            print(f"-----------------------------------------------------------------------------------------")
            print(f"------finish process exchange document-----")

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

def upServerToReceivDocEncrypted(conf, server_cert_chain, server_key, host, local_port):
    print(f"------Up {conf.configuration.client_name}'s server to receive a document-----")
    server = Server(conf, server_cert_chain, server_key, host, local_port)

def upClienteToSendDocumentEncripted(conf,serverName, client_cert_chain, client_key, host, port):
    ssl_client_file = ClientSSL(conf, client_cert_chain, client_key, host, port)
    ssl_client_file.sock_connect(serverName)
    ssl_client_file.send_recv_file(conf.configuration.config_client.cliente_file)
    ssl_client_file.conn.close()

def process_encryption(conf):
    print(f"-----------------------------------------------------------------------------------------")
    print(f"------Begin process encryption {conf.configuration.client_name}'s document-----")

    if conf:
        module = Server(conf, conf.configuration.config_server.server_cert_chain, conf.configuration.config_server.server_key, conf.configuration.server_name, conf.configuration.local_port )
        print(f" --> 1 - {conf.configuration.client_name} start your Attestable")
        time.sleep(2)

        ssl_client_file = ClientSSL(conf, conf.configuration.config_client.client_cert_chain, conf.configuration.config_client.client_key, conf.configuration.server_name, conf.configuration.local_port)
        ssl_client_file.sock_connect(conf.configuration.client_name)
        ssl_client_file.send_recv_file(conf.configuration.config_client.cliente_file)
        #ssl_client_file.conn.close()
        time.sleep(2)

    print(f"------Finish process encryption {conf.configuration.client_name}'s document-----")
    time.sleep(6)


def open_notepad():
    os.system("start notepad")


def exit_program():
    exit()


if __name__ == '__main__':
    main()
