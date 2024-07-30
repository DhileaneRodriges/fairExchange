import hashlib
import socket
import threading
import time

from appDhully.client.Client import ClientSSL


class PBBService():
    def __int__(self):
        pass

    def startProcess(self):
        print(f"-----------------------------------------------------------------------------------------")
        print(f"------Begin PBB process -----")

        # Start the server in a new thread
        server_thread = threading.Thread(target=self.startPbbServer, name="pbb_server")
        server_thread.start()
        time.sleep(2)

        alice_thread = threading.Thread(target=self.upClienteToSendSignalToPBB, name="client_alice", args=("Alice", b'123', "positive"))
        alice_thread.start()
        time.sleep(2)
        #self.upClienteToSendSignalToPBB("Alice", b'123', "positive")
        self.upClienteToSendSignalToPBB("Bob", b'123', "negative")

        print(f"-----------------------------------------------------------------------------------------")
        print(f"------finish PBB process-----")
    def startPbbServer(self):

        # Create a socket object
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Get local machine name
        host = socket.gethostname()

        # Choose a port that is free
        port = 1234

        # Bind to the port
        server_socket.bind((host, port))

        # Queue up to 5 requests
        server_socket.listen(5)

        # Dictionary to store client messages and sockets
        client_messages = {}
        client_sockets = {}

        # Dictionary to store sent messages
        sent_messages = {}

        while True:
            # Establish a connection
            client_socket, addr = server_socket.accept()

            print("Got a connection from %s" % str(addr))

            # Receive data from the client
            data = client_socket.recv(1024)
            client_name, client_hash, message = data.decode().split(',')

            # Check if the client has sent the same message before to the same hash
            if client_name in sent_messages and client_hash in sent_messages[client_name] and message in \
                    sent_messages[client_name][client_hash]:
                print(f"The client {client_name} tried to send the same message again to the same hash.")
                client_socket.close()
                continue

            print(f"Received {message} from the client {client_name} with hash {client_hash}")

            # Add the message to the record of sent messages
            if client_name not in sent_messages:
                sent_messages[client_name] = {}
            if client_hash not in sent_messages[client_name]:
                sent_messages[client_name][client_hash] = set()
            sent_messages[client_name][client_hash].add(message)

            # If a client with the same hash has already sent a message
            if client_hash in client_messages:
                # Process the messages
                result = PBBService.process_messages([client_messages[client_hash], (client_name, client_hash, message)])

                # Send the result to both clients
                for socketIt in [client_sockets[client_hash], client_socket]:
                    socketIt.send(result.encode())
                    socketIt.close()

                # Remove the processed messages
                del client_messages[client_hash]
                del client_sockets[client_hash]
            else:
                # Store the client message and socket for later processing
                client_messages[client_hash] = (client_name, client_hash, message)
                client_sockets[client_hash] = client_socket
    def process_messages(messages):
        # Implement your message processing logic here
        # For example, if both messages are 'positive', return 'positive'
        if all(message[2] == 'positive' for message in messages):
            return 'positive'
        else:
            return 'negative'

    def upClienteToSendSignalToPBB(self, clientName, key, signal):
        # Create a socket object
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Set a timeout of 5 seconds
        #client_socket.settimeout(30)

        # Get local machine name
        host = socket.gethostname()

        # Choose the same port as the server
        port = 1234

        # Connect to the server
        client_socket.connect((host, port))

        # Send a message to the server
        client_name = clientName
        hash_object = hashlib.sha256(key)
        hex_dig = hash_object.hexdigest()
        message = f'{client_name},{hex_dig},{signal}'
        client_socket.send(message.encode())

        # Wait for the response from the server
        try:
            while True:
                response = client_socket.recv(1024)
                if response:
                    print("Client %s received : %s of server" % (clientName, response.decode()))
                    break
        except socket.timeout:
            print('Timeout occurred, the message will be removed...')
            remove_message = f'{client_name},{hex_dig},remove'
            client_socket.send(remove_message.encode())

        # Close the connection with the server
        client_socket.close()
