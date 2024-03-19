import socket

receber = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
receber.bind(("localhost", 7777))
print("ouvindo conexao")
receber.listen(10)
connection, address = receber.accept()

namefile = connection.recv(1024).decode()
with open(namefile, 'rb') as file:
    for data in file.readlines():
        connection.send(data)

    print('Arquivo Enviado')


