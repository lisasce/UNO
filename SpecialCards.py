from NormalCards import Cards
#weils sein vater ist


class SpecialCards(Cards):
    listOfSpecialCards = []
    def __init__(self, name,color,number, func):
        self.name = name
        super(number, color)
        self.func = func
        SpecialCards.listOfSpecialCards.append(self)

def changeColor():
    pass


# plus2B = SpecialCards('+2', 'blue', 2)
# plus2Y = SpecialCards('+2', 'yellow', 2)
# plus2R = SpecialCards('+2', 'red', 2)
# plus2G = SpecialCards('+2', 'green', 2)
# plus4N = SpecialCards('+4', None, 4)
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

