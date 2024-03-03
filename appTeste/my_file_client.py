# my_file_client.py
import os
import socket
import ssl
from pathlib import Path


from file_common import FileCommon

class FileClient(FileCommon):
    def run_client(self, file_path):
        #context = ssl.SSLContext()
        context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)

        RESOURCE_DIRECTORY = Path(__file__).resolve().parent.parent / 'certskeys' / 'client'
        CLIENT_CERT_CHAIN = RESOURCE_DIRECTORY / 'aliceClient.intermediate.chain.pem'
        CLIENT_KEY = RESOURCE_DIRECTORY / 'aliceClient.key.pem'

        context.load_cert_chain(certfile=CLIENT_CERT_CHAIN, keyfile=CLIENT_KEY, password="Camb")
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ssl_socket = context.wrap_socket(client_socket)

        try:
            ssl_socket.connect(("localhost", 8080))

            # Envia o nome do arquivo
            filename = os.path.basename(file_path)
            ssl_socket.send(filename.encode())

            # Recebe o conteúdo criptografado do arquivo
            ciphertext = ssl_socket.recv(1024)

            # Descriptografa o conteúdo do arquivo
            decryption_key = b'your-secret-key'  # Substitua por uma chave secreta forte
            plaintext = self.decrypt_file(ciphertext, decryption_key)

            # Salva o arquivo descriptografado
            with open("decrypted_" + filename, 'wb') as file:
                file.write(plaintext)

            print("Arquivo descriptografado salvo com sucesso:", "decrypted_" + filename)
        finally:
            ssl_socket.close()
