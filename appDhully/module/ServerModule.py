
import socket
import ssl
import threading
import select
from appDhully.module.client_handler import ClientHandler


class Module():
  def __init__(self, config):

    self.config = config
    print("\nServer running Alice's attestable ... Its PEM pass phrase is: camb\n")
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile=self.config.SERVER_CERT_CHAIN, keyfile=self.config.SERVER_KEY)

    self.context = context
    self.server_name = self.config.SERVER_NAME
    self.local_port = self.config.LOCAL_PORT

    server_socket = socket.socket()
    server_socket.bind((self.server_name, self.local_port))
    server_socket.listen(5)
    rd_list = [server_socket]  # include server_socket in list
    wr_list = []  # empty list
    er_list = []  # empty list

    print("Server has been started inside Alice's attestable running on host: ", self.server_name)
    print("It is listening on port {0}...".format(self.local_port))

    server_socket_open = "YES"
    while server_socket_open == "YES":
      readable, writable, errored = select.select(rd_list, wr_list, er_list)
      for s in readable:
        if s is server_socket:
          client_socket, address = server_socket.accept()
          try:
            # Wrap the socket in an SSL connection (will perform a handshake)
            conn = self.context.wrap_socket(client_socket, server_side=True)
            # start the thread in a new thread
            threading.start_new_thread(self.handle_connection, (conn, self.config))
          except ssl.SSLError as e:
            print(e)




