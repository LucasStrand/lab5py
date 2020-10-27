import random

while True:
    print ('Make your choice: ')
    choice = input()
    choice = choice.lower()
    print("My choice is", choice)

    choices = ['rock','paper','scissors']
    computerChoice = random.choice(choices)
    print ("Computer choice is", computerChoice)

    choiceDict = {'rock': 0, 'paper': 1, 'scissors':2}

    choiceIndex = choiceDict.get(choice, 3)
    computerIndex = choiceDict.get(computerChoice)

    resultMatrix = [[0,2,1],
                    [1,0,2],
                    [2,1,0],
                    [3,3,3]]

    resultIdx = resultMatrix[choiceIndex][computerIndex]

    resultMessages = ['it is a tie', 'You win!', 'You lose', 'Invalid choice, try again']

    result = resultMessages[resultIdx]

    print(result)