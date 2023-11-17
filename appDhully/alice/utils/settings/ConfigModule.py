import argparse
from pathlib import Path

class ConfigAliceModule:
  def __init__(self):


    self.parser = argparse.ArgumentParser(description="Alice's server running inside Alice's attestable")
    self.parser.add_argument("-s", "--server_name", help="localhost", default="localhost")
    self.parser.add_argument("-p", "--port_number", help="port used by server", default="8290")
    self.parser.add_argument("-f", "--file_to_send", help="file to send to client", default="alicedoc_encrypted.txt")

    # self.LOCAL_HOST = 'localhost'
    self.SERVER_NAME = "localhost"
    self.LOCAL_PORT = 8290
    self.RESOURCE_DIRECTORY = Path(__file__).resolve().parent.parent.parent.parent.parent / 'certskeys' / 'server'
    self.SERVER_CERT_CHAIN = self.RESOURCE_DIRECTORY / 'attAlice.intermediate.chain.pem'
    self.SERVER_KEY = self.RESOURCE_DIRECTORY / 'attAlice.key.pem'

    # three new lines
    # receive 4096 bytes each time
    self.BUFFER_SIZE = 4096
    self.SEPARATOR = "<SEPARATOR>"
    self.RECV_FILE_NAME_PREFIX = ""
