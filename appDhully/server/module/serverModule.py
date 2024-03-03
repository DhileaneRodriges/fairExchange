import socket
import ssl
import threading
import select
from pathlib import Path

from appDhully.server.Utils.client_handler import ClientHandler

class Module():
    def __init__(self, configurations):

        config = configurations.config.config_server
        CERTKEYS_DIRECTORY = Path(__file__).resolve().parent.parent.parent.parent / 'certskeys' / 'server'

        context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        context.load_cert_chain(certfile= CERTKEYS_DIRECTORY/config.server_cert_chain,
                                keyfile=CERTKEYS_DIRECTORY/config.server_key, password="camb")

        self.configurations = configurations
        self.context = context
        self.server_name = configurations.config.server_name
        self.local_port = configurations.config.local_port

        self.server_socket = socket.socket()
        self.server_socket.bind((self.server_name, self.local_port))
        self.server_socket.listen(5)
        self.rd_list = [self.server_socket]  # include server_socket in list
        self.wr_list = []  # empty list
        self.er_list = []  # empty list

        # Cria uma thread para aceitar conexões
        aceitar_thread = threading.Thread(target=self.accept_connection)
        aceitar_thread.start()
        print(f"Server has been started inside {configurations.config.client_name}'s attestable running on host: {self.server_name}")
        print(f"It is listening on port {self.local_port}...")
        print(aceitar_thread.name)

    def accept_connection(self):
        server_socket_open = True
        while server_socket_open:
            readable, _, _ = select.select(self.rd_list, self.wr_list, self.er_list)
            for s in readable:
                if s is self.server_socket:
                    client_socket, _ = self.server_socket.accept()
                    try:
                        conn = self.context.wrap_socket(client_socket, server_side=True)
                        #ClientHandler(conn, self.configurations).start()
                        self.server_socket.close()  # close the server socket or hang
                        server_socket_open = False  # close and loop again: produces
                    except ssl.SSLError as e:
                        print(e)
    def receiv_file(self, conn):
        ClientHandler(conn, self.configurations).start()
