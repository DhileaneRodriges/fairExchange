import argparse
from pathlib import Path

class ConfigServerModule:
  def __init__(self, server_cert_chain, server_key, ):

    self.server_cert_chain = server_cert_chain
    self.server_key = server_key