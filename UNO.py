import random
import time
from NormalCards import Cards
#die unteren 2 wollen sich nicht importieren lassen :(
from SpecialCards import SpecialCards
from UnoFunctions import *


def givingCards():
    card = (random.choice(listOfNormalCards))
    gameStock.append(card)
    listOfCards.remove(card)
    for c in range (1,3):
        card = (random.choice(listOfCards))
        userCards.append(card)
        listOfCards.remove(card)
    for c in range (1,3):
        card = (random.choice(listOfCards))
        computerCards.append(card)
        listOfCards.remove(card)
    for c in range (1,3):
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
    global actionExecuted
    playersName = usersName
    #showingUsersCards()
    gameStockCard =showingGameStock()
    if actionExecuted == False:
        actionExecuted=isItASpecialCard(gameStockCard, SpecialCards, userCards, listOfCards, playersName,gameStock)
    showingUsersCards()
    usersChoice= userInput()
    if usersChoice == None:
        pickedCards = pickingCard(userCards, listOfCards, playersName)
        print('for info your new card is:', ', '.join([str(card) for card in pickedCards]))
        time.sleep(2)
    elif usersChoice.number == gameStockCard.number or usersChoice.color == \
            gameStockCard.color or usersChoice.color == None:
        if usersChoice.color == None:
            userChoosingColor(usersChoice, colors)
        gameStock.append(usersChoice)
        userCards.remove(usersChoice)
        if isinstance(card, SpecialCards):
            actionExecuted = False
        print('good choice!','\n')
        if len(userCards) == 1:
            print('UNOOOOOO you have only 1 card left!')
        elif len(userCards) == 0:
            print(playersName, 'won! end of the game!')
            return False # game ends
        time.sleep(2)
        #showingGameStock()
    else:
        pickingCard(userCards, listOfCards, playersName)
        print('your new card is:', str(card))
    return True

def computersTurn():
    global actionExecuted
    playersName = 'Computer'
    gameStockCard =showingGameStock()
    if actionExecuted == False:
        actionExecuted =isItASpecialCard(gameStockCard, SpecialCards, computerCards, listOfCards, playersName,gameStock)
    cardFound = False
    print("Computer's turn:")
    for c in computerCards:
        if c.number == gameStockCard.number or c.color == gameStockCard.color \
                or c.color == None:
            cardFound = True
            if c.color == None:
                c.color = automaticChoosingColor(computerCards, colors)
            print('computer plays: ',c)
            gameStock.append(c)
            computerCards.remove(c)
            if isinstance(card, SpecialCards):
                actionExecuted = False
            if len(computerCards) == 1:
                print('Computer says: UNOOOOOO guys!')
            elif len(computerCards) == 0:
                print('Computer won! end of the game!')
                return False
            time.sleep(2)
            break
    if cardFound == False:
        pickingCard(computerCards, listOfCards, playersName)
    return True

def fritzsTurn():
    global actionExecuted
    playersName = 'Fritz'
    gameStockCard =showingGameStock()
    if actionExecuted == False:
        actionExecuted = isItASpecialCard(gameStockCard, SpecialCards, fritzCards, listOfCards, playersName,gameStock)
    cardFound = False
    print("Fritz's turn:")
    for c in fritzCards:
        if c.number == gameStockCard.number or c.color == gameStockCard.color\
                or c.color == None:
            cardFound = True
            if c.color == None:
                c.color = automaticChoosingColor(fritzCards, colors)
            time.sleep(2)
            print('Fritz plays: ',c)
            gameStock.append(c)
            fritzCards.remove(c)
            if isinstance(card, SpecialCards):
                actionExecuted = False
            if len(fritzCards) == 1:
                print('Fritz says: UNOOOOOO guys!')
            elif len(fritzCards) == 0:
                print('Fritz won! end of the game!')
                return False
            time.sleep(2)
            break
    if cardFound == False:
        pickingCard(fritzCards, listOfCards, playersName)
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


playersTurns = []
listOfNormalCards = Cards.normalCardGenerator()
listOfSpecialCards = SpecialCards.listOfSpecialCards
listOfCards = listOfNormalCards + listOfSpecialCards
computerCards = []
userCards = []
gameStock = []
fritzCards = []
colors= ['blue', 'red', 'green', 'yellow']
directionChanged = False
actionExecuted = False


usersName = input("Welcome to UNO, what's your name ? \n")
print('Hi', usersName, ", let's play!")

card = (random.choice(listOfCards))
playersTurns.append(usersTurn)
playersTurns.append(computersTurn)
playersTurns.append(fritzsTurn)


#print(listOfCards)

givingCards()
game()
