import socket


def serversideGetPlaySocket():
    sockS = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    sockS.bind(('127.0.0.1', 60003))
    sockS.listen(1)

    # server is never shut down, we listen adn listen and listen ...
    while True:
        print('\nlistening...\n')
        (sockC, addr) = sockS.accept()
        print('connection from {}'.format(addr))
        
        while True:
            serversidedPlayerInput = playerChoice()
            print('Your choice ',serversidedPlayerInput, '\nPlease wait for the other player to make a move')
            data = sockC.recv(1024)
            if not data:
                break
            clientsidedPlayer = data.decode('ascii')
            serverDidWin, clientDidWin = checkWin(serversidedPlayerInput,clientsidedPlayer)
            if serverDidWin:
                answer = 'serversided win!\n'
            elif clientDidWin:
                answer = 'clientsided win!\n'
            else:
                answer = 'a draw\n'

            results = 'Server chose ' + serversidedPlayerInput + ' and the client ' + clientsidedPlayer + ' and the game resulted in a ' + answer
            print(results)
            sockC.sendall(bytearray(results, 'ascii'))
        
        sockC.close()
        print('client {} disconnected'.format(addr))


def clientsideGetPlaySocket(host):
    sockC = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    sockC.connect(('127.0.0.1', 60003))
    while True:

        message = playerChoice()
        sockC.sendall(bytearray(message, 'ascii'))
        print('Your choice: ', message, '\nPlease wait for the other player to make a move.')

        data = sockC.recv(1024)
        #print("Opponent's choice:", data.decode('ascii'))
        print('received:', data.decode('ascii'))
    sockC.close()

def playerChoice():
    message = "?"
    message = message.lower()
    choices = ['r','p','s']
    while message not in choices:
        message = input('Make your choice: (r)Rock, (p)Paper, (s)Sissors: ')
    return message

def checkWin(serversidedPlayer, clientsidedPlayer):

    isServersidedWin = False
    isClientsidedWin = False
    
    if serversidedPlayer == clientsidedPlayer:
        return isServersidedWin, isClientsidedWin
    elif serversidedPlayer == "r":
        if clientsidedPlayer == "p":
            isClientsidedWin = True
            return isServersidedWin, isClientsidedWin
        else:
            isServersidedWin = True
            return isServersidedWin, isClientsidedWin
    elif serversidedPlayer == "p":
        if clientsidedPlayer == "s":
            isClientsidedWin = True
            return isServersidedWin, isClientsidedWin
        else:
            isServersidedWin = True
            return isServersidedWin, isClientsidedWin
    elif serversidedPlayer == "s":
        if clientsidedPlayer == "r":
            isClientsidedWin = True
            return isServersidedWin, isClientsidedWin
        else:
            isServersidedWin = True
            return isServersidedWin, isClientsidedWin


ans = "?"
while ans not in {"C","S"}:
    ans = input("Do you wanna be server (S) or client (C): ")

if ans=="S":
    sock = serversideGetPlaySocket()
else:
    host = input("Enter the server's name or IP:")
    sock = clientsideGetPlaySocket(host)