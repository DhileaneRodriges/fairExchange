
import socket
import ssl
import threading
import select
from appDhully.server.client_handler import ClientHandler


class Module():
  def __init__(self, configurations):

    self.config = configurations.configServers
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile=configurations.configServers.config_server.server_cert_chain, keyfile=configurations.configServers.config_server.server_key, password="camb")

    self.context = context
    self.server_name = configurations.configServers.server_name
    self.local_port = configurations.configServers.local_port

    self.server_socket = socket.socket()
    self.server_socket.bind((self.server_name, self.local_port))
    self.server_socket.listen(5)
    self.rd_list = [self.server_socket]  # include server_socket in list
    self.wr_list = []  # empty list
    self.er_list = []  # empty list

    # Cria uma thread para aceitar conexões
    aceitar_thread = threading.Thread(target=accep_conection, args=(self,))
    aceitar_thread.start()
    print("  Server has been started inside " + self.config.client_name + "'s attestable running on host: ", self.server_name)
    print("  It is listening on port {0}...".format(self.local_port))

    print("  " + aceitar_thread.name)

def accep_conection(self):
  server_socket_open = "YES"
  while server_socket_open == "YES":
    readable, writable, errored = select.select(self.rd_list, self.wr_list, self.er_list)
    for s in readable:
      if s is self.server_socket:
        client_socket, address = self.server_socket.accept()
        try:

          conn = self.context.wrap_socket(client_socket, server_side=True)
          ClientHandler(conn, self.config).start()
          self.server_socket.close()  # close the server socket or hang
          server_socket_open = "NO"  # close and loop again: produces
        except ssl.SSLError as e:
          print(e)




