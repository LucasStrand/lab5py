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
            print('Your choice ', serversidedPlayerInput)
            data = sockC.recv(1024)
            if not data:
                break
            clientsidedPlayer = data.decode('ascii')
            serverDidWin, clientDidWin = checkWin(serversidedPlayerInput,clientsidedPlayer)
            if serverDidWin:
                answer = 'Server won!'
            elif clientDidWin:
                answer = 'Client won!'
            else:
                answer = "It's a draw nigger"

            print('received:', data.decode('ascii'))
            #answer = 'thanks for the data!'
            sockC.sendall(bytearray(answer, 'ascii'))
            print('answered:', answer)
        
        sockC.close()
        print('client {} disconnected'.format(addr))


def clientsideGetPlaySocket(host):
    sockC = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    sockC.connect(('127.0.0.1', 60003))
    while True:

        message = playerChoice()
        sockC.sendall(bytearray(message, 'ascii'))
        print('Your choice: ', message, 'Please wait for the other player to make a move.')

        data = sockC.recv(1024)
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
            return isClientsidedWin
        else:
            isServersidedWin = True
            return isServersidedWin, isClientsidedWin
    elif serversidedPlayer == "s":
        if clientsidedPlayer == "r":
            isClientsidedWin = True
            return isServersidedWin, isClientsidedWin
        else:
            isServersidedWin = False
            return isServersidedWin, isClientsidedWin


ans = "?"
while ans not in {"C","S"}:
    ans = input("Do you wanna be server (S) or client (C): ")

if ans=="S":
    sock = serversideGetPlaySocket()
else:
    host = input("Enter the server's name or IP:")
    sock = clientsideGetPlaySocket(host)





    # Row is serversidedPlayer and column is clientsidedPlayer
#              rock 0      paper 1   scissors 2
#              ___________________________________
#rock-> 0     |____0____|_____2______|______1_____|
#paper-> 1    |____1____|_____0______|______2_____|
#scissors-> 2 |____2____|_____1______|______0_____|
#invalid-> 3  |____3____|_____3______|______3_____|
# # 0= tied, 1= client win, 2= server win, 3= invalid


# choiceDict = {'rock': 0, 'paper': 1, 'scissors':2}

#     serversidedPlayerIndex = choiceDict.get(choice, 3)
#     clientsidedPlayerIndex = choiceDict.get(choice, 3)

#     resultMatrix = [[0,2,1],
#                     [1,0,2],
#                     [2,1,0],
#                     [3,3,3]]

#     resultIdx = resultMatrix[serversidedPlayerIndex][clientsidedPlayerIndex]

#     resultMessages = ['it is a tie', 'Client won!', 'Server won!', 'Invalid choice, try again']
    
#     result = resultMessages[resultIdx]