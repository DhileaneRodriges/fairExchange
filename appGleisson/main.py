# main.py
import threading

from file_server import FileServer
from file_client import FileClient

def main():
    encryption_key = b'your-secret-key'  # Substitua por uma chave secreta forte

    file_server = FileServer(encryption_key)
    file_client = FileClient()

    # Inicia o servidor em uma thread
    server_thread = threading.Thread(target=file_server.run_server)
    server_thread.start()

    # Espera um pouco para garantir que o servidor seja iniciado antes do cliente
    import time
    time.sleep(1)

    # Executa o cliente
    file_path = "caminho/do/seu/arquivo.txt"  # Substitua pelo caminho do seu arquivo
    file_client.run_client(file_path)

if __name__ == "__main__":
    main()
