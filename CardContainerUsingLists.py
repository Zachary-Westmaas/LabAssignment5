from CardContainer import CardContainer
from Card import IntCard
class Node:
    def __init__(self, data):
        self.__data =  data
        self.__next = None
    def get_next (self):
        return self.__next
    def set_next(self,value):
        self.__next = value
    def get_Data(self):
        return self.__data


class CardCnterUsingLists(CardContainer):

    def __init__(self):
        super().__init__()
        self.__initNumofCards = None
        self.__head = None
    def setInitNumofCards(self, n):
        self.__initNumofCards = n

    def addNewCards(self,listOfC):
        self.__cardsUser = listOfC
        lofc = listOfC.copy()
        list = IntCard()
        for line in lofc:
            cardList = line
            if line[1] == 'A':
                cardList = (line[0],'14')
            elif line[1] == 'J':
                cardList = (line[0],'11')
            elif line[1] == 'Q':
                cardList = (line[0],'12')
            elif line[1] == 'K':
                cardList = (line[0],'13')
            else:
                cardList = (line[0],line[1])
            if line[0] == 'Clubs':
                cardList = (int(cardList[1]) - 1)
            elif line[0] == 'Diamonds':
                cardList = (int(cardList[1]) - 1 + 12)
            elif line[0] == 'Hearts':
                cardList = (int(cardList[1]) - 1 + (12 * 2))
            elif line[0] == 'Spades':
                cardList = (int(cardList[1]) - 1 + (12 * 3))
            list.set_value(cardList)
            node = self.__head
            if node == None:
                self.__head = Node(list)
            else:
                while not node.get_next() == None:
                    node = node.get_next()

                node.set_next(Node(list))
    def addNewCard(self,c):
        list = IntCard()
        node = self.__head
        if node == None:
            list.set_value(c)
            self.__head = Node(list)
        else:
            while not node.get_next() == None:
                node = node.get_next()
            node.set_next(Node(list))
    def get_cards(self):
        local = []
        node = self.__head

        while not node == None:
            local.append(node.get_Data().get_value())
            node = node.get_next()
        return local
    def get_cards_from_userview(self):
        node = self.__head
        local = []
        while not node == None:
            value = node.get_Data().get_value()
            suit = ''
            print(value)
            if node.get_Data().get_value() >=1 and node.get_Data().get_value() <=13:
                suit = 'Clubs'
                value +=1
                if value == 14:
                    value = 'A'
                elif value == 11:
                    value = 'J'
                elif value == 12:
                    value = 'Q'
                elif value == 13:
                    value = 'K'
                else:
                    value = str(value)
            elif node.get_Data().get_value() >= 14 and node.get_Data().get_value() <= 26:
                suit = 'Diamonds'
                value +=1
                value -=13
                if value == 14:
                    value = 'A'
                elif value == 11:
                    value = 'J'
                elif value == 12:
                    value = 'Q'
                elif value == 13:
                    value = 'K'
                else:
                    value = str(value)
            elif node.get_Data().get_value() >= 27 and node.get_Data().get_value() <= 39:
                suit = 'Hearts'
                value += 1
                value -= 26
                if value == 14:
                    value = 'A'
                elif value == 11:
                    value = 'J'
                elif value == 12:
                    value = 'Q'
                elif value == 13:
                    value = 'K'
                else:
                    value = str(value)
            elif node.get_Data().get_value() >= 40 and node.get_Data().get_value() <=52:
                suit = 'Spades'
                value += 1
                value -= 39
                if value == 14:
                    value = 'A'
                elif value == 11:
                    value = 'J'
                elif value == 12:
                    value = 'Q'
                elif value == 13:
                    value = 'K'
                else:
                    value = str(value)
            local = local.append((suit, value))
            node = node.get_next()
    def remove_first_card(self):
        node = self.__head
        self.__head = self.__head.get_next()
        return node.get_Data()
