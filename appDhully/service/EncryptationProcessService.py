import threading
import time
from asyncio import threads

import psutil

from appDhully.client.Client import ClientSSL
from appDhully.server.ServerSSL import ServerSSL


class EncryptationProcessService():
    def __init__(self):
        pass

    def startProcess(self, conf):
        self.conf = conf
        if self.conf is None:
            return False
        try:
            print(f"-----------------------------------------------------------------------------------------")
            print(f"------Begin process encryption {self.conf.configuration.client_name}'s document-----")

            server_thread = threading.Thread(target=self.start_server, name="encryption_server")
            server_thread.start()

            client, received_file = self.start_client()

            print(f"------Finish process encryption {conf.configuration.client_name}'s document-----")
            time.sleep(2)

            return True, received_file
        except Exception as e:
            print(f"An error occurred during the encryption process: {e}")
            return False, None

    def start_server(self):
        server = ServerSSL(self.conf, self.conf.configuration.config_server.server_cert_chain,
                  self.conf.configuration.config_server.server_key,
                  "uploadFile",
                  self.conf.configuration.server_name,
                  self.conf.configuration.local_port, None, True)
        print(f" --> 1 - {self.conf.configuration.client_name} start your Attestable")

        return server

    def start_client(self):
        client = ClientSSL(self.conf, self.conf.configuration.config_client.client_cert_chain,
                           self.conf.configuration.config_client.client_key, self.conf.configuration.server_name,
                           self.conf.configuration.local_port, True)

        client.sock_connect("attestable " + self.conf.configuration.client_name + " CAMB")
        received_file = client.send_and_receive_encrypted_file( self.conf.configuration.path_file / self.conf.configuration.config_client.cliente_file)

        return client, self.conf.configuration.path_file/ received_file
