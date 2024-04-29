import threading
import time

from appDhully.alice.Configurations import ConfigsAlice
from appDhully.bob.Configurations import ConfigsBob
from appDhully.client.Client import ClientSSL
from appDhully.server.ServerSSL import ServerSSL


class ExchangeEncryptedFile():
    def __int__(self):
        pass

    def startProcess(self, conf1, conf2, encrypted_file_Alice, encrypted_file_Bob):
        print(f"-----------------------------------------------------------------------------------------")
        print(f"------Begin process exchange document-----")

        # Start the server in a new thread
        server_thread = threading.Thread(target=self.upServerToReceivDocEncrypted,
                                         args=(conf1, conf1.configuration.config_server.intermadiate_server_cert_chain,
                                               conf1.configuration.config_server.intermadiate_server_key,
                                               conf1.configuration.server_name, 8290, encrypted_file_Bob))
        server_thread.start()

        self.upClienteToSendDocumentEncripted(conf2, conf1.configuration.client_name + " Server CAMB",
                                              conf2.configuration.config_client.intermadiate_client_cert_chain,
                                              conf2.configuration.config_client.intermadiate_client_key,
                                              conf1.configuration.server_name, 8290, encrypted_file_Alice)

        print(f"-----------------------------------------------------------------------------------------")
        print(f"------finish process exchange document-----")
    def upServerToReceivDocEncrypted(self, conf, server_cert_chain, server_key, host, local_port):

        print(f"------Up {conf.configuration.client_name}'s server to receive a document-----")
        server = ServerSSL(conf, server_cert_chain, server_key, "exchangeEncryptedFiles", host, local_port)

    def upClienteToSendDocumentEncripted(self, conf, serverName, client_cert_chain, client_key, host, port):

        ssl_client_file = ClientSSL(conf, client_cert_chain, client_key, host, port)
        ssl_client_file.sock_connect(serverName)
        ssl_client_file.exchange_encrypted_file(
            conf.configuration.path_file / conf.configuration.config_server.server_file)
        ssl_client_file.conn.close()
