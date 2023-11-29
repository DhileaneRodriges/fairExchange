# file_client.py
import socket
import ssl

from file_common import FileCommon

class FileClient(FileCommon):
    def run_client(self, file_path):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ssl_socket = ssl.wrap_socket(client_socket, cert_reqs=ssl.CERT_NONE, ssl_version=ssl.PROTOCOL_TLS)

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
