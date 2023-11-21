import argparse
from pathlib import Path
from appDhully.Utils.ConfigModule import ConfigServerModule

class ConfigBobModule:
  def __init__(self):
    SERVER_NAME = "localhost"
    LOCAL_PORT = 8290
    CLIENT_NAME = "Bob"
    parser = argparse.ArgumentParser(description="Bob's server running inside Bob's attestable")
    parser.add_argument("-s", "--server_name", help="localhost", default=SERVER_NAME)
    parser.add_argument("-p", "--port_number", help="port used by server", default=LOCAL_PORT)
    parser.add_argument("-f", "--file_to_send", help="file to send to client", default="helloServer.txt")

    RESOURCE_DIRECTORY = Path(__file__).resolve().parent.parent.parent / 'certskeys' / 'server'
    SERVER_CERT_CHAIN = RESOURCE_DIRECTORY / 'attAlice.intermediate.chain.pem'
    SERVER_KEY = RESOURCE_DIRECTORY / 'attAlice.key.pem'

    # three new lines
    # receive 4096 bytes each time
    BUFFER_SIZE = 4096
    SEPARATOR = "<SEPARATOR>"
    RECV_FILE_NAME_PREFIX = ""

    self.configServerModule = ConfigServerModule(SERVER_NAME, LOCAL_PORT, CLIENT_NAME, parser, RESOURCE_DIRECTORY,
                       SERVER_CERT_CHAIN, SERVER_KEY, BUFFER_SIZE, SEPARATOR, RECV_FILE_NAME_PREFIX);
