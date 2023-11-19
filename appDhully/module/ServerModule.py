
import socket
import ssl
import threading
import select
from appDhully.module.client_handler import ClientHandler


class Module():
  def __init__(self, config):

    self.config = config
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile=self.config.SERVER_CERT_CHAIN, keyfile=self.config.SERVER_KEY, password="camb")

    self.context = context
    self.server_name = self.config.SERVER_NAME
    self.local_port = self.config.LOCAL_PORT

    self.server_socket = socket.socket()
    self.server_socket.bind((self.server_name, self.local_port))
    self.server_socket.listen(5)
    self.rd_list = [self.server_socket]  # include server_socket in list
    self.wr_list = []  # empty list
    self.er_list = []  # empty list

    print("Server has been started inside "+self.config.CLIENT_NAME+"'s attestable running on host: ", self.server_name)
    print("It is listening on port {0}...".format(self.local_port))
    # Cria uma thread para aceitar conexões
    aceitar_thread = threading.Thread(target=accep_conection, args=(self,))
    aceitar_thread.start()
    print(aceitar_thread.name)

def accep_conection(self):
  server_socket_open = "YES"
  while server_socket_open == "YES":
    readable, writable, errored = select.select(self.rd_list, self.wr_list, self.er_list)
    for s in readable:
      if s is self.server_socket:
        client_socket, address = self.server_socket.accept()
        try:
          # Wrap the socket in an SSL connection (will perform a handshake)
          conn = self.context.wrap_socket(client_socket, server_side=True)
          # start the thread in a new thread
          self.handle_connection, (conn, self.config)
        except ssl.SSLError as e:
          print(e)




