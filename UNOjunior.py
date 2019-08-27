from NormalCards import Cards
import random
import time


def givingCards():
    card = (random.choice(listOfCards))
    gameStock.append(card)
    listOfCards.remove(card)
    for c in range (1,8):
        card = (random.choice(listOfCards))
        userCards.append(card)
        listOfCards.remove(card)
    for c in range (1,8):
        card = (random.choice(listOfCards))
        computerCards.append(card)
        listOfCards.remove(card)
    for c in range (1,8):
        card = (random.choice(listOfCards))
        fritzCards.append(card)
        listOfCards.remove(card)

def showingUsersCards():
    time.sleep(1)
    print('\nYour cards are:')
    for c in userCards:
        print(c, end='; ')
    print('\n')

def showingGameStock():
    c = gameStock[len(gameStock)-1]
    time.sleep(1)
    print('the card in the middle is:', c, '\n')
    gameStockCard = c
    return c

def userInput():
    usersChoice = input('Please write the chosen card to play, '
                        '\nif nothing fits, press enter:\n')
    for c in userCards:
        if usersChoice == str(c):
            return c
    if usersChoice == '':
        return None
    userInput()

def usersTurn():
    gameStockCard =showingGameStock()
    usersChoice= userInput()
    if usersChoice == None:
        card = (random.choice(listOfCards))
        userCards.append(card)
        listOfCards.remove(card)
        print('you just picked a new card:', str(card), 'your turn is over')
        time.sleep(2)
    elif usersChoice.number == gameStockCard.number or usersChoice.color == gameStockCard.color:
        gameStock.append(usersChoice)
        userCards.remove(usersChoice)
        print('good choice!','\n')
        if len(userCards) == 1:
            print('UNOOOOOO you have only 1 card left!')
        elif len(userCards) == 0:
            print('You won! end of the game!')
            return False
        time.sleep(2)
        #showingGameStock()
    else:
        card = (random.choice(listOfCards))
        userCards.append(card)
        listOfCards.remove(card)
        print('you just picked a new card:', str(card), 'your turn is over')
        time.sleep(2)
    return True

def computersTurn():
    playersName = 'Computer'
    gameStockCard =showingGameStock()
    cardFound = False
    print("Computer's turn:")
    for c in computerCards:
        if c.number == gameStockCard.number or c.color == gameStockCard.color:
            cardFound = True
            time.sleep(2)
            print('computer plays: ',c)
            gameStock.append(c)
            computerCards.remove(c)
            if len(computerCards) == 1:
                print('Computer says: UNOOOOOO guys!')
            elif len(computerCards) == 0:
                print('Computer won! end of the game!')
                return False
            time.sleep(2)
            break
    if cardFound == False:
        card = (random.choice(listOfCards))
        computerCards.append(card)
        listOfCards.remove(card)
        print('the',playersName, 'just picked a new card.\n')
        print('Now, this turn is over. \n')
        time.sleep(2)
    return True

def fritzsTurn():
    gameStockCard =showingGameStock()
    cardFound = False
    print("Fritz's turn:")
    for c in fritzCards:
        if c.number == gameStockCard.number or c.color == gameStockCard.color:
            cardFound = True
            time.sleep(2)
            print('Fritz plays: ',c)
            gameStock.append(c)
            fritzCards.remove(c)
            if len(fritzCards) == 1:
                print('Fritz says: UNOOOOOO guys!')
            elif len(fritzCards) == 0:
                print('Fritz won! end of the game!')
                return False
            time.sleep(2)
            break
    if cardFound == False:
        card = (random.choice(listOfCards))
        fritzCards.append(card)
        listOfCards.remove(card)
        print('Fritz just picked a new card, his turn is over.\n')
        time.sleep(2)
    return True

def game():
    gameNotFinished = True
    while gameNotFinished:
        if len(listOfCards) == 0:
            for c in gameStock:
                listOfCards.append(c)
                gameStock.remove(c)

        for playerIndex in range(0,len(playersTurns)):
            player=playersTurns[playerIndex]
            gameNotFinished = player()
            if directionChanged == True:
                playerIndex = playersTurns.index(player)+1
            if gameNotFinished == False:
                break


            showingUsersCards()

playersTurns = []
listOfNormalCards = Cards.normalCardGenerator()
listOfSpecialCards = []
listOfCards = listOfNormalCards + listOfSpecialCards
computerCards = []
userCards = []
gameStock = []
fritzCards = []
directionChanged = False

card = (random.choice(listOfCards))
playersTurns.append(computersTurn)
playersTurns.append(fritzsTurn)
playersTurns.append(usersTurn)



givingCards()
showingUsersCards()
game()
