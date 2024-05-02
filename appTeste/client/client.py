import socket
import time

HOST = "localhost"  # Endereço do servidor
PORT = 8000  # Porta do servidor
HEARTBEAT_INTERVAL = 5
HEARTBEAT_TIMEOUT = HEARTBEAT_INTERVAL * 2  # Tempo limite para heartbeat (em segundos)

def send_file(filename):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))

        # Enviar arquivo para o servidor
        with open(filename, "rb") as file:
            for data in iter(lambda: file.read(1024), b""):
                client_socket.sendall(data)

        # Monitorar heartbeats do servidor
        last_heartbeat_time = time.time()
        while True:
            try:
                data = client_socket.recv(1024)
                if data == b"HEARTBEAT":
                    last_heartbeat_time = time.time()

                # Verificar se o tempo limite do heartbeat foi excedido
                if time.time() - last_heartbeat_time > HEARTBEAT_TIMEOUT:
                    print("Heartbeat do servidor perdido. Upload possivelmente falhou.")
                    break

            except Exception as e:
                print(f"Erro ao comunicar com o servidor: {e}")
                break

        print("Upload do arquivo concluído.")

if __name__ == "__main__":
    filename = "arquivo.txt"  # Nome do arquivo a ser enviado
    send_file(filename)


