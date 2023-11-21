import argparse
from pathlib import Path
from appDhully.Utils.Configurations import ConfigServers
from appDhully.Utils.ConfigModule import ConfigServerModule
from appDhully.Utils.ConfigClient import ConfigClientModule

class ConfigsAlice:

  def __init__(self):
    server_name = "localhost"
    local_port = 8290
    client_name = "Alice"
    buffer_size = 4096
    separator = "<SEPARATOR>"
    recv_file_name_prefix = ""
    headersize = 10

    resource_directory = Path(__file__).resolve().parent.parent.parent / 'certskeys' / 'server'
    server_cert_chain = resource_directory / 'attAlice.intermediate.chain.pem'
    server_key = resource_directory / 'attAlice.key.pem'

    parserServer = argparse.ArgumentParser(description="Alice's server running inside Alice's attestable")
    parserServer.add_argument("-s", "--server_name", help="localhost", default=server_name)
    parserServer.add_argument("-p", "--port_number", help="port used by server", default=local_port)
    parserServer.add_argument("-f", "--file_to_send", help="file to send to client", default="alicedoc_encrypted.txt")

    configServerModule = ConfigServerModule( resource_directory, server_cert_chain, server_key, parserServer)

    resource_directory_client = Path(__file__).resolve().parent.parent.parent / 'certskeys' / 'client'
    client_cert_chain = resource_directory_client / 'aliceClient.intermediate.chain.pem'
    client_key = resource_directory_client / 'aliceClient.key.pem'
    ca_cert = resource_directory_client / 'rootca.cert.pem'

    configClientModule = ConfigClientModule( resource_directory_client, client_cert_chain, client_key, ca_cert)

    self.configServers = ConfigServers(server_name, local_port, client_name, separator, buffer_size, headersize, recv_file_name_prefix, configServerModule, configClientModule);
