import threading
import time

from appDhully.client.Client import ClientSSL
from appDhully.server.ServerSSL import ServerSSL


class EncryptationProcessService():
    def __int__(self):
        pass

    def startProcess(self, conf):
        self.conf = conf
        print(f"-----------------------------------------------------------------------------------------")
        print(f"------Begin process encryption {self.conf.configuration.client_name}'s document-----")

        if self.conf:
            module = ServerSSL(self.conf, self.conf.configuration.config_server.server_cert_chain,
                               self.conf.configuration.config_server.server_key,
                               "uploadFile",
                               self.conf.configuration.server_name,
                               self.conf.configuration.local_port)
            print(f" --> 1 - {self.conf.configuration.client_name} start your Attestable")
            time.sleep(2)

            ssl_client_file = ClientSSL(conf, conf.configuration.config_client.client_cert_chain,
                                        conf.configuration.config_client.client_key, conf.configuration.server_name,
                                        conf.configuration.local_port)
            ssl_client_file.sock_connect("attestable " + conf.configuration.client_name + " CAMB")
            ssl_client_file.send_recv_file(conf.configuration.config_client.cliente_file)
            # ssl_client_file.conn.close()
            time.sleep(2)

        print(f"------Finish process encryption {conf.configuration.client_name}'s document-----")
        time.sleep(3)
