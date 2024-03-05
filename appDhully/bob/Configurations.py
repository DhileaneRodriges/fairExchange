import argparse
from pathlib import Path
from appDhully.Utils.Configurations import Configuration
from appDhully.Utils.ConfigServer import ConfigServerModule
from appDhully.Utils.ConfigClient import ConfigClientModule

class ConfigsBob:

  def __init__(self):
    server_name = "localhost"
    local_port = 8291
    client_name = "Bob"
    buffer_size = 4096
    separator = "<SEPARATOR>"
    recv_file_name_prefix = ""
    headersize = 10
    path_file = Path(__file__).resolve().parent / "files"
    server_file = "bobdoc_encrypted.txt"
    cliente_file = "helloServer.txt"

    resource_directory = Path(__file__).resolve().parent.parent.parent / 'certskeys' / 'server'

    server_cert_chain = resource_directory / 'attBob.intermediate.chain.pem'
    server_key = resource_directory / 'attBob.key.pem'

    intermadiate_server_cert_chain = resource_directory / 'bobServer.intermediate.chain.pem'
    intermadiate_server_key = resource_directory / 'bobServer.key.pem'

    parserServer = argparse.ArgumentParser(description="Bob's server running inside Bob's attestable")
    parserServer.add_argument("-s", "--server_name", help="localhost", default=server_name)
    parserServer.add_argument("-p", "--port_number", help="port used by server", default=local_port)
    parserServer.add_argument("-f", "--file_to_send", help="file to send to client", default=server_file)

    configServerModule = ConfigServerModule( resource_directory, server_cert_chain, server_key, intermadiate_server_cert_chain,  intermadiate_server_key,  parserServer, server_file)

    resource_directory_client = Path(__file__).resolve().parent.parent.parent / 'certskeys' / 'client'
    client_cert_chain = resource_directory_client / 'bobClient.intermediate.chain.pem'
    client_key = resource_directory_client / 'bobClient.key.pem'

    intermadiate_client_cert_chain = resource_directory_client / 'bobClient.intermediate.chain.pem'
    intermadiate_client_key = resource_directory_client / 'bobClient.key.pem'
    ca_cert = resource_directory_client / 'rootca.cert.pem'


    clientParser = argparse.ArgumentParser(description="Bob app acting as a client")
    clientParser.add_argument("-s", "--server", help="Host where Bob's attestablei run, default is localhost",
                        default=server_name)
    clientParser.add_argument("-p", "--port", help="Server port, default is ", default=local_port)
    clientParser.add_argument("-f", "--file", help="File to send to server, default is helloServer.txt",
                        default=cliente_file)

    configClientModule = ConfigClientModule( resource_directory_client, client_cert_chain, client_key, intermadiate_client_cert_chain, intermadiate_client_key, ca_cert, clientParser, cliente_file)

    self.configuration = Configuration(server_name, local_port, client_name, path_file, separator, buffer_size, headersize, recv_file_name_prefix, configServerModule, configClientModule)
