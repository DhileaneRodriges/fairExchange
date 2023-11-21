import argparse
from pathlib import Path

class ConfigServerModule:
  def __init__(self, resource_directory, server_cert_chain, server_key, parserServer,server_file):

    self.resource_directory = resource_directory
    self.server_cert_chain = server_cert_chain
    self.server_key = server_key
    self.parserServer = parserServer
    self.server_file = server_file
