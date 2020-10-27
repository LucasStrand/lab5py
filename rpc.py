 import socket

 sockS = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
 sockS.bind(('127.0.0.1', 60003))
 sockS.listen(1)

# server is never shut up down, we listen adn listen and listen ...

while True:
    print('\nlistening...\n')
    (sockC, addr) = sockS.accept()
    print('connection from {}'.format(addr))
    while True:
        data = sockC.recv(1024)
        if not data:
            break
        print('received:', data.decode('ascii'))
        answer = 'thanks for the data!'
        sockC.sendall(bytearray(answer,'ascii'))
        print('answered:', answer)
    sockC.close()
    print('client {} disconnected'.format(addr))

# def serversideGetPlaySocket():
#     pass

# def clientsideGetPlaySocket(host):
#     pass

# ans = "?"
# while ans not in {"C","S"}:
#     ans = input("Do you wanna be server (S) or client (C): ")

# if ans=="S":
#     sock = serversideGetPlaySocket()
# else:
#     host = input("Enter the server's name or IP:")
#     sock = clientsideGetPlaySocket(host)