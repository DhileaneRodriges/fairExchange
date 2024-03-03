import argparse
from pathlib import Path

class ConfigServers:
  def __init__(self, server_name, local_port, client_name, cliente_file, path_cliente_file, config_server, config_client ):

    self.server_name = server_name
    self.local_port = local_port
    self.client_name = client_name
    self.cliente_file = cliente_file
    self.path_cliente_file = path_cliente_file

    self.config_server = config_server
    self.config_client = config_client
