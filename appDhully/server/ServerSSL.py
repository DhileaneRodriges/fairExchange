import socket
import ssl
import threading
import select
from appDhully.server.Utils.client_handler import ClientHandler

class ServerSSL():
    def __init__(self, configurations, server_cert_chain, server_key, option_service, host, port):
        """Initializes the server with the given configurations."""
        self.config = configurations.configuration
        self.context = self.create_context(server_cert_chain, server_key)
        self.server_name = host
        self.local_port = port
        self.server_socket = self.create_server_socket()
        self.rd_list = [self.server_socket]
        self.wr_list = []
        self.er_list = []

        self.accept_connections(option_service)

    def create_context(self, server_cert_chain, server_key):
        """Creates and returns a new SSL context."""
        context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        context.load_cert_chain(certfile=server_cert_chain, keyfile=server_key, password="camb")
        return context

    def create_server_socket(self):
        """Cria e retorna um novo socket de servidor."""
        server_socket = socket.socket()
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((self.server_name, self.local_port))
        server_socket.listen(5)
        return server_socket

    def accept_connections(self, callBack):
        """Accepts new connections and starts a new ClientHandler for each one."""
        server_socket_open = True
        while server_socket_open:
            readable, _, _ = select.select(self.rd_list, self.wr_list, self.er_list)
            for s in readable:
                if s is self.server_socket:
                    client_socket, _ = self.server_socket.accept()
                    self.handle_new_connection(client_socket, callBack)
                    server_socket_open = False

    def handle_new_connection(self, client_socket, callBack):
        """Wraps a new connection in SSL and starts a new ClientHandler."""
        try:
            conn = self.context.wrap_socket(client_socket, server_side=True)
            ClientHandler(conn, self.config, callBack).start()
        except ssl.SSLError as e:
            print(e)
        finally:
            self.server_socket.close()

    def handle_encrypted_file(self, conn):
        """Receives a file, encrypts it and sends it back."""
        # Receive file from client
        file_data = conn.recv(1024)
        # Encrypt the file data
        encrypted_data = self.encrypt_file_data(file_data)
        # Send the encrypted file back to the client
        conn.sendall(encrypted_data)

    def encrypt_file_data(self, file_data):
        """Encrypts the file data and returns it."""
        # Implement your encryption logic here
        encrypted_data = file_data  # Replace this with your encryption logic
        return encrypted_data
    def close_socket(self):
        """Closes the server socket."""
        if self.server_socket is not None:
            self.server_socket.close()
