class Card():
    def __init__(self):
        pass
    def isLargerThan(self,c):
        pass
    def print_card(self):
        pass
class IntCard(Card):
    def __init__(self):
        super().__init__()
        self.__value = None
    def set_value(self,card):
        self.__value = card
    def isLargerThan(self,c):
        valueOne = int(self.__value)
        valueOne = (valueOne - 1)%13
        valueTwo = int(c)
        valueTwo = (valueTwo - 1)%13
        if valueOne > valueTwo:
            return True
        else:
            return False
    def get_value(self):
        return self.__value







