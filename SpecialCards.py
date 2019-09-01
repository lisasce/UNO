from UnoFunctions import pickingCard
from NormalCards import Cards
#weils sein vater ist


class SpecialCards(Cards):
    listOfSpecialCards = []
    def __init__(self, name,color,number, func):
        self.name = name
        super().__init__(number, color)
        self.func = func
        SpecialCards.listOfSpecialCards.append(self)
    def __str__(self):
        if self.color == None:
            return ('{self.name}').format(self=self)
        return ('{self.name}'+ '-' +'{self.color}').format(self=self)

def changeColor(playersCards,listOfCards,playersName, gameStock):
    pass

def plus4(playersCards,listOfCards,playersName, gameStock):

    for card in playersCards:
        if isinstance(card, SpecialCards) and card.name == '+2' \
                and card.color == gameStock[len(gameStock)-1]:
            gameStock.append(card)
            playersCards.remove(card)
            return
        elif isinstance(card, SpecialCards) and card.name == '+4':
            gameStock.append(card)
            playersCards.remove(card)
            return
    pickingCard(playersCards, listOfCards, playersName, 4)

def plus2(playersCards,listOfCards,playersName, gameStock):
    for card in playersCards:
        if isinstance(card, SpecialCards) and card.name == '+2':
            gameStock.append(card)
            playersCards.remove(card)
            return
    pickingCard(playersCards,listOfCards,playersName,2)



plus2B = SpecialCards('+2', 'blue', 2, plus2)
plus2Y = SpecialCards('+2', 'yellow', 2, plus2)
plus2R = SpecialCards('+2', 'red', 2, plus2)
plus2G = SpecialCards('+2', 'green', 2, plus2)
plus4 = SpecialCards('+4', None, 4, plus4)
changeColor = SpecialCards('change color', None, None, changeColor)
# changeDirectionB = SpecialCards('change direction', 'blue', None)
# changeDirectionY = SpecialCards('change direction', 'yellow', None)
# changeDirectionR = SpecialCards('change direction', 'red', None)
# changeDirectionG = SpecialCards('change direction', 'green', None)
# passTurnB = SpecialCards('no turn', 'blue', None, noTurn)
# passTurnY = SpecialCards('no turn', 'yellow', None, noTurn)
# passTurnR = SpecialCards('no turn', 'red', None, noTurn)
# passTurnG = SpecialCards('no turn', 'green', None,noTurn)

#print(SpecialCards.listOfSpecialCards)

