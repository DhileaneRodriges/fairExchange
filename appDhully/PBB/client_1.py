import socket

def start_client():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get local machine name
    host = socket.gethostname()

    # Choose the same port as the server
    port = 12345

    # Connect to the server
    client_socket.connect((host, port))

    # Send a message to the server
    message = 'positive'  # or 'negative'
    client_socket.send(message.encode())

    # Wait for the response from the server
    while True:
        response = client_socket.recv(1024)
        if response:
            print("The server responded with: %s" % response.decode())
            break

    # Close the connection with the server
    client_socket.close()

if __name__ == "__main__":
    start_client()