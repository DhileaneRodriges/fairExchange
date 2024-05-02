import threading
class ClientHandler(threading.Thread):
    def __init__(self, client_socket):
        threading.Thread.__init__(self)
        self.client_socket = client_socket

    def run(self):
        while True:
            # Receber dados do cliente
            try:
                data = self.client_socket.recv(1024)
                if not data:
                    break

                # Processar dados do cliente (se necessário)

                # Enviar mensagem de heartbeat ao cliente
                self.send_heartbeat()
            except Exception as e:
                print(f"Erro ao comunicar com o cliente: {e}")
                break

        # Fechar o socket do cliente
        self.client_socket.close()

    def send_heartbeat(self):
        heartbeat_message = "HEARTBEAT".encode()
        self.client_socket.sendall(heartbeat_message)
