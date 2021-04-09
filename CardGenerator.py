import random
class CardGenerator():
    def __init__(self):
        self.__listOne = None
        self.__listTwo = None
        self.__dispNumOne = None
        self.__dispNumTwo = None
    def generateCards(self,n):
        cardsOne = []
        cardsTwo = []
        while n > 26 or n <= 0:
            n = int(input('please enter a valid number between 0 and 26:'))
        else:
            for num in range(n):
                randOne = random.randint(2, 53)
                randTwo = random.randint(2, 53)
                while randOne == randTwo or randTwo in cardsOne or randOne in cardsTwo or randOne in cardsOne or randTwo in cardsTwo:
                    randTwo = random.randint(2, 53)
                    randOne = random.randint(2, 53)
                else:
                    cardsOne.append(randOne)
                    cardsTwo.append(randTwo)
            self.__listOne = cardsOne
            self.__listTwo = cardsTwo
            listOne = cardsOne.copy()
            listTwo = cardsTwo.copy()
            for line in cardsOne:
                if line >= 2 and line <= 14:
                    x = line
                    listOne[listOne.index(line)] = ('Clubs', str(x))
                    if x < 11:
                        x = str(line)
                    elif x == 11:
                        x = 'J'
                    elif x == 12:
                        x = 'Q'
                    elif x == 13:
                        x = 'K'
                    elif x == 14:
                        x = 'A'
                    cardsOne[cardsOne.index(line)] = ('Clubs', str(x))
                elif line >= 15 and line <= 27:
                    x = line - 13
                    listOne[listOne.index(line)] = ('Diamonds', str(x))
                    if x < 11:
                        x = str(x)
                    elif x == 11:
                        x = 'J'
                    elif x == 12:
                        x = 'Q'
                    elif x == 13:
                        x = 'K'
                    elif x == 14:
                        x = 'A'
                    cardsOne[cardsOne.index(line)] = ('Diamonds', str(x))
                elif line >= 28 and line <= 40:
                    x = line - 13 * 2
                    listOne[listOne.index(line)] = ('Hearts', str(x))
                    if x < 11:
                        x = str(x)
                    elif x == 11:
                        x = 'J'
                    elif x == 12:
                        x = 'Q'
                    elif x == 13:
                        x = 'K'
                    elif x == 14:
                        x = 'A'
                    cardsOne[cardsOne.index(line)] = ('Hearts', str(x))
                elif line >= 41 and line <= 53:
                    x = line - 13 * 3
                    listOne[listOne.index(line)] = ('Spades', str(x))
                    if x < 11:
                        x = str(x)
                    elif x == 11:
                        x = 'J'
                    elif x == 12:
                        x = 'Q'
                    elif x == 13:
                        x = 'K'
                    elif x == 14:
                        x = 'A'
                    cardsOne[cardsOne.index(line)] = ('Spades', str(x))
            for line in cardsTwo:
                if line >= 2 and line <= 14:
                    x = line
                    listTwo[listTwo.index(line)] = ('Clubs', str(x))
                    if x < 11:
                        x = str(line)
                    elif x == 11:
                        x = 'J'
                    elif x == 12:
                        x = 'Q'
                    elif x == 13:
                        x = 'K'
                    elif x == 14:
                        x = 'A'
                    cardsTwo[cardsTwo.index(line)] = ('Clubs', str(x))
                elif line >= 15 and line <= 27:
                    x = line - 13
                    listTwo[listTwo.index(line)] = ('Diamonds', str(x))
                    if x < 11:
                        x = str(x)
                    elif x == 11:
                        x = 'J'
                    elif x == 12:
                        x = 'Q'
                    elif x == 13:
                        x = 'K'
                    elif x == 14:
                        x = 'A'
                    cardsTwo[cardsTwo.index(line)] = ('Diamonds', str(x))
                elif line >= 28 and line <= 40:
                    x = line - 13 * 2
                    listTwo[listTwo.index(line)] = ('Hearts', str(x))
                    if x < 11:
                        x = str(x)
                    elif x == 11:
                        x = 'J'
                    elif x == 12:
                        x = 'Q'
                    elif x == 13:
                        x = 'K'
                    elif x == 14:
                        x = 'A'
                    cardsTwo[cardsTwo.index(line)] = ('Hearts', str(x))
                elif line >= 41 and line <= 53:
                    x = line - 13 * 3
                    listTwo[listTwo.index(line)] = ('Spades', str(x))
                    if x < 11:
                        x = str(x)
                    elif x == 11:
                        x = 'J'
                    elif x == 12:
                        x = 'Q'
                    elif x == 13:
                        x = 'K'
                    elif x == 14:
                        x = 'A'
                    cardsTwo[cardsTwo.index(line)] = ('Spades', str(x))
            self.__dispNumOne = listOne
            self.__dispNumTwo = listTwo
        return cardsOne , cardsTwo
    def get_listOne(self):
        return self.__listOne
    def get_listTwo(self):
        return self.__listTwo
    def get_dispNumOne(self):
        return self.__dispNumOne
    def get_dispNumTwo(self):
        return self.__dispNumTwo