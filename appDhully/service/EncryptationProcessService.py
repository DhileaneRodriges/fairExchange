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
            return

        print(f"-----------------------------------------------------------------------------------------")
        print(f"------Begin process encryption {self.conf.configuration.client_name}'s document-----")

        server_thread = threading.Thread(target=self.start_server, name="server")
        server_thread.start()

        client = self.start_client()

        print(f"------Finish process encryption {conf.configuration.client_name}'s document-----")
        time.sleep(2)

    def start_server(self):
        server = ServerSSL(self.conf, self.conf.configuration.config_server.server_cert_chain,
                  self.conf.configuration.config_server.server_key,
                  "uploadFile",
                  self.conf.configuration.server_name,
                  self.conf.configuration.local_port)
        print(f" --> 1 - {self.conf.configuration.client_name} start your Attestable")

        return server

    def start_client(self):
         client = ssl_client_file = ClientSSL(self.conf, self.conf.configuration.config_client.client_cert_chain,
                       self.conf.configuration.config_client.client_key, self.conf.configuration.server_name,
                       self.conf.configuration.local_port)

         ssl_client_file.sock_connect("attestable " + self.conf.configuration.client_name + " CAMB")
         ssl_client_file.send_recv_file(self.conf.configuration.config_client.cliente_file)

         return client