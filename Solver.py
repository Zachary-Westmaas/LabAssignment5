
class Solver():
    def __init__(self):
        self.__pOne = None
        self.__pTwo = None
        self.__table = None
        self.__printResult = None
    def setPrint_Result(self,p):
        self.__printResult = p
    def solve(self):
        count = 0
        checkOne = False
        checkTwo = False
        while count <= 100 and checkOne == False and checkTwo == False :
            count+=1
            pOne = self.__pOne.remove_first_card()
            pTwo = self.__pTwo.remove_first_card()
            self.__table.addNewCard(pOne)
            self.__table.addNewCard(pTwo)
            self.__printResult.print_step(count, self.__pOne, self.__pTwo,self.__table)
            if pOne.isLarger(pTwo):
                while not self.__table.__head == None:
                    self.__pOne.addNewCard(self.__table.remove_first_card())
            elif pTwo.isLarger(pOne):
                while not self.__table.__head == None:
                    remOne = self.__table.remove_first_card()
                    remTwo = self.__table.remove_first_card()
                    self.__pTwo.addNewCard(remTwo)
                    self.__pTwo.addNewCard(remOne)
            else:
                # Assume they both have enough cards
                if self.__pOne.__head == None:
                    checkOne = True
                if self.__pTwo.__head == None:
                    checkTwo = True
                if checkOne:
                    res = 1
                    self.__printResult.set_res(res)
                    self.__printResult.set_num_moves(count)
                    self.__printResult.print_output()
                elif checkTwo:
                    res = 2
                    self.__printResult.set_res(res)
                    self.__printResult.set_num_moves(count)
                    self.__printResult.print_output()
                elif checkOne and checkTwo:
                    self.__printResult.set_num_moves(count)
                    self.__printResult.print_output()

                else:
                    pOne = self.__pOne.remove_first_card()
                    pTwo = self.__pTwo.remove_first_card()
                    pThree = self.__pOne.remove_first_card()
                    pFour = self.__pTwo.remove_first_card()
                    self.__table.addNewCard(pOne)
                    self.__table.addNewCard(pTwo)
                    self.__table.addNewCard(pThree)
                    self.__table.addNewCard(pFour)
                    if pOne.isLarger(pTwo):
                        while not self.__table.__head == None:
                            self.__pOne.addNewCard(self.__table.remove_first_card())
                    elif pTwo.isLarger(pOne):
                        while not self.__table.__head == None:
                            remOne = self.__table.remove_first_card()
                            remTwo = self.__table.remove_first_card()
                            self.__pTwo.addNewCard(remTwo)
                            self.__pTwo.addNewCard(remOne)


    def set_playerOne(self, RPOne):
        self.__pOne = RPOne
    def set_playerTwo(self, RPTwo):
        self.__pTwo = RPTwo
    def set_table(self, tbl):
        self.__table = tbl