import time

from appDhully.client.Client import ClientSSL
from appDhully.server.ServerSSL import ServerSSL


def startProcess(conf):
    print(f"-----------------------------------------------------------------------------------------")
    print(f"------Begin process encryption {conf.configuration.client_name}'s document-----")

    if conf:
        module = ServerSSL(conf, conf.configuration.config_server.server_cert_chain,
                           conf.configuration.config_server.server_key, conf.configuration.server_name,
                           conf.configuration.local_port)
        print(f" --> 1 - {conf.configuration.client_name} start your Attestable")
        time.sleep(2)

        ssl_client_file = ClientSSL(conf, conf.configuration.config_client.client_cert_chain,
                                    conf.configuration.config_client.client_key, conf.configuration.server_name,
                                    conf.configuration.local_port)
        ssl_client_file.sock_connect()
        ssl_client_file.send_recv_file(conf.configuration.config_client.cliente_file)
        # ssl_client_file.conn.close()
        time.sleep(2)

    print(f"------Finish process encryption {conf.configuration.client_name}'s document-----")
    time.sleep(6)
    pass
