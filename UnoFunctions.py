import random
import time


def pickOneCard (playersCards,listOfCards,playersName):
    card = (random.choice(listOfCards))
    playersCards.append(card)
    listOfCards.remove(card)
    print(playersName, 'just picked a new card.\n')
    print('Turn is over. \n')
    time.sleep(2)

def isItASpecialCard(gameStockCard, Specialcards):
    if isinstance(gameStockCard, Specialcards):
        gameStockCard.func()
    else:
        pass

def choosingColor(playersCards):
        return playersCards[0].color


def userChoosingColor(usersChoice, colors):
        chosenColor = input('Which color do you choose '
                            '(blue, red, green or yellow):\n').lower()
        if chosenColor in colors:
            usersChoice.color = chosenColor
        else:
            userChoosingColor()
