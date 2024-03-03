import argparse
from pathlib import Path

class ConfigClientModule:
  def __init__(self, client_cert_chain, client_key, ca_cert):

    self.client_cert_chain = client_cert_chain
    self.client_key = client_key
    self.ca_cert = ca_cert