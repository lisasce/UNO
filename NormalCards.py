#test
class Cards:
    def __init__(self,number, color):
        self.number = number
        self.color = color
        #self.colorShortName = colorShortName
    def __str__(self):
        return ('{self.number}'+ '-' +'{self.color}').format(self=self)

    @staticmethod
    #bedeutet die folgende Funktion gehört nur zur Klasse nicht zu jedem Objekt
    def normalCardGenerator():
            listOfNormalCards = []
            for j in range(1, 3):
                for i in range(1, 10):
                    listOfNormalCards.append(Cards(i, 'blue'))
                    listOfNormalCards.append(Cards(i, 'yellow'))
                    listOfNormalCards.append(Cards(i, 'red'))
                    listOfNormalCards.append(Cards(i, 'green'))
            listOfNormalCards.append(Cards(0, 'blue'))
            listOfNormalCards.append(Cards(0, 'yellow'))
            listOfNormalCards.append(Cards(0, 'red'))
            listOfNormalCards.append(Cards(0, 'green'))
            return listOfNormalCards
            # cards from 1 to 9 in each color x2, 1x card 0
            #print(len(listOfNormalCards))
