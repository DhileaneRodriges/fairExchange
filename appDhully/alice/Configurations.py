import argparse
from pathlib import Path
from appDhully.server.Utils.Configurations import ConfigServers
from appDhully.server.Utils.ConfigModule import ConfigServerModule
from appDhully.server.Utils.ConfigClient import ConfigClientModule

class ConfigsAlice:

  def __init__(self):
    server_name = "localhost"
    local_port = 8290
    client_name = "Alice"

    cliente_file = "helloServer.txt"
    path_cliente_file =  Path(__file__).resolve().parent /'files'


    server_cert_chain = 'attAlice.intermediate.chain.pem'
    server_key = 'attAlice.key.pem'

    configServerModule = ConfigServerModule( server_cert_chain, server_key)

    client_cert_chain = 'aliceClient.intermediate.chain.pem'
    client_key = 'aliceClient.key.pem'
    ca_cert = 'rootca.cert.pem'

    configClientModule = ConfigClientModule( client_cert_chain, client_key, ca_cert)

    self.config = ConfigServers(server_name, local_port, client_name, cliente_file,path_cliente_file, configServerModule, configClientModule);
