import socket
import threading
import time
import ClientHandler

HOST = "localhost"  # Endereço do servidor
PORT = 8000  # Porta do servidor
HEARTBEAT_INTERVAL = 5
def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(5)

        while True:
            client_socket, address = server_socket.accept()
            print(f"Cliente conectado: {address}")

            # Criar e iniciar thread para gerenciar o cliente
            client_handler = ClientHandler(client_socket)
            client_handler.start()
if __name__ == "__main__":
    start_server()



