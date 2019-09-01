import random
import time


def pickingCard (playersCards,listOfCards,playersName, numberToPick=1):
    pickedCards = []
    for c in range(0,numberToPick):
        card = (random.choice(listOfCards))
        playersCards.append(card)
        listOfCards.remove(card)
        pickedCards.append(card)
    print(playersName, 'just picked', numberToPick, 'new card(s).\n')
    print('Turn is over. \n')
    time.sleep(2)
    return pickedCards


def isItASpecialCard(gameStockCard, Specialcards, playersCards, listOfCards, playersName, gameStock):
    if isinstance(gameStockCard, Specialcards):
        gameStockCard.func(playersCards, listOfCards, playersName, gameStock)
        return True
    else:
        return False




def userChoosingColor(usersChoice, colors):
        chosenColor = input('Which color do you choose '
                            '(blue, red, green or yellow):\n').lower()
        if chosenColor in colors:
            usersChoice.color = chosenColor
        else:
            userChoosingColor()


def automaticChoosingColor(playersCards, colors):
    for card in playersCards:
        if card.color in colors:
            chosenColor = card.color
            print('you did choose: ', chosenColor, '\n')
            return chosenColor




