import socket
import ssl
import threading
from pathlib import Path
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from file_common import FileCommon

class FileServer(FileCommon):
    def __init__(self, encryption_key):
        super().__init__()
        self.encryption_key = encryption_key
        self.certskeys = Path(__file__).resolve().parent.parent / 'certskeys' / 'server'

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

            # Cria um contexto SSL
            #context = ssl.SSLContext()
            context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)

            SERVER_CERT_CHAIN = self.certskeys / 'aliceServer.intermediate.chain.pem'
            SERVER_KEY = self.certskeys / 'aliceServer.key.pem'

            context.load_cert_chain(certfile=SERVER_CERT_CHAIN, keyfile=SERVER_KEY)
            # Envolve o socket do cliente com SSL
            ssl_socket = context.wrap_socket(client_socket)

            # Inicia uma thread para lidar com o cliente
            client_thread = threading.Thread(target=self.handle_client, args=(ssl_socket,))
            client_thread.start()
