import argparse
class ModuleSettings:
  def __init__(self):

    self.parser = argparse.ArgumentParser(description="Alice's server running inside Alice's attestable")
    self.parser.add_argument("-s", "--server_name", help="localhost", default="localhost")
    self.parser.add_argument("-p", "--port_number", help="port used by server", default="8290")
    self.parser.add_argument("-f", "--file_to_send", help="file to send to client", default="alicedoc_encrypted.txt")
    self.run();
  def run(self):
    args = self.parser.parse_args()
    server_name = args.server_name
    port_number = args.port_number
    file_to_send = args.file_to_send

    server = SSLserverfile()