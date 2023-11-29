# file_server.py
import socket
import ssl
import threading
from pathlib import Path


from file_common import FileCommon

class FileServer(FileCommon):
    def __init__(self, encryption_key):
        super().__init__()
        self.encryption_key = encryption_key
        self.server_cert = Path(__file__).resolve().parent.parent / 'certskeys' / 'server' / 'attAlice.intermediate.chain.pem'

    def handle_client(self, conn):
        try:
            # Recebe o nome do arquivo
            filename = conn.recv(1024).decode()
            print("Recebendo arquivo:", filename)

            # Criptografa o conteúdo do arquivo
            ciphertext = self.encrypt_file(filename, self.encryption_key)

            # Envia o conteúdo criptografado do arquivo
            conn.sendall(ciphertext)

            print("Arquivo criptografado enviado com sucesso:", filename)
        except Exception as e:
            print("Erro ao enviar o arquivo criptografado:", e)
        finally:
            conn.close()

    def run_server(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(("localhost", 8080))
        server_socket.listen(5)

        print("Servidor SSL iniciado. Aguardando conexões...")

        while True:
            client_socket, addr = server_socket.accept()
            ssl_socket = ssl.wrap_socket(client_socket, server_side=True, certfile="server.crt",  ssl_version=ssl.PROTOCOL_TLS)

            # Inicia uma thread para lidar com o cliente
            client_thread = threading.Thread(target=self.handle_client, args=(ssl_socket,))
            client_thread.start()
