# This is a sample Python script.
import result
import CardGenerator
from CardContainerUsingLists import CardCnterUsingLists
from Solver import Solver
from result import Print_Result
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n = int(input('Enter the amount of cards from 0 to 26:'))
    genCard = CardGenerator.CardGenerator()
    listOne,listTwo = genCard.generateCards(n)
    print(listOne)
    print(listTwo)
    temp = CardCnterUsingLists()
    u1 = CardCnterUsingLists()
    u2 = CardCnterUsingLists()
    u1.addNewCards(listOne)
    u2.addNewCards(listTwo)
    solveOne = Solver()
    solveOne.set_playerOne(u1)
    solveOne.set_playerTwo(u2)
    solveOne.set_table(temp)
    result = Print_Result()
    solveOne.setPrint_Result(result)
    res, num_moves = solveOne.solve()
    result.set_res(res)
    result.set_nummoves(num_moves)
    print("Game Over!\n")
    result.print_output()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
