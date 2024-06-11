import socket

def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get local machine name
    host = socket.gethostname()

    # Choose a port that is free
    port = 12345

    # Bind to the port
    server_socket.bind((host, port))

    # Queue up to 5 requests
    server_socket.listen(5)

    # List to store client messages and sockets
    client_messages = []
    client_sockets = []

    while True:
        # Establish a connection
        client_socket, addr = server_socket.accept()

        print("Got a connection from %s" % str(addr))

        # Receive data from the client
        data = client_socket.recv(1024)
        print("Received %s from the client" % data.decode())

        # Store the client message
        client_messages.append(data.decode())
        client_sockets.append(client_socket)

        # If two clients have sent their messages
        if len(client_messages) == 2:
            # Process the messages
            result = process_messages(client_messages)

            # Send the result to both clients
            for socketIt in client_sockets:
                socketIt.send(result.encode())
                socketIt.close()

            # Clear the client messages
            client_messages.clear()
            client_sockets.clear()


def process_messages(messages):
    # Implement your message processing logic here
    # For example, if both messages are 'positive', return 'positive'
    if all(message == 'positive' for message in messages):
        return 'positive'
    else:
        return 'negative'

if __name__ == "__main__":
    start_server()