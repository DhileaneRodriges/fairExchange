import socket
import ssl
import os
from pathlib import Path

from appDhully.server.Utils.files2sockets import recv_store_file

class SSLClientFile():
    def __init__(self, config_client):

        self.config = config_client.config.config_client

        self.client_name = config_client.config.client_name
        self.server = config_client.config.server_name
        self.port = config_client.config.local_port
        self.soc = None
        self.conn = None
        self.CERTS_DIRECTORY = Path(__file__).resolve().parent.parent.parent.parent / 'certskeys' / 'client'

    def sock_connect(self):

        self.soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Create a standard TCP Socket
        # Create SSL context which holds the parameters for any sessions
        context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)


        context.load_verify_locations(self.CERTS_DIRECTORY / self.config.ca_cert)
        context.load_cert_chain(certfile=self.CERTS_DIRECTORY / self.config.client_cert_chain,
                                keyfile=self.CERTS_DIRECTORY / self.config.client_key, password="camb")

        # We can wrap in an SSL context first, then connect
        self.conn = context.wrap_socket(self.soc, server_hostname="attestable " + self.client_name + " CAMB")

        # OK 27Jul2023
        self.conn.connect((self.server, self.port))
    def send_file(self, module, file_name):

        # Read file to be sent
        with open(file_name, "rb") as file:
            file_data = file.read()

        # Send file data
        self.conn.sendall(file_data)

        print("File sent successfully.")

    def recv_file(self, file_name):
        try:

            # This method uses the already connected conn socket
            print("Negotiated session using cipher suite: {0}\n".format(self.conn.cipher()[0]))

            print("cli-request_file.py: before send")
            self.conn.send(b"Send me your encrypted doc!\n")
            print("cli-request_file.py: after send")

            print("cli_file_flie.py now waiting from string from ser_file_file.py")

            received = self.conn.recv(self.config_client.configServers.buffer_size).decode()
            remote_filename, filesize = received.split(self.config_client.configServers.separator)
            remote_filename = os.path.basename(remote_filename)
            remote_filename = self.config_client.configServers.recv_file_name_prefix + remote_filename
            filesize = int(filesize)
            recv_store_file(remote_filename, filesize, self.config_client.configServers.buffer_size, self.conn)
            print("cli_file_flie.py has received file from ser_file_file.py")

        finally:
            if self.conn is not None:
                self.conn.close()
