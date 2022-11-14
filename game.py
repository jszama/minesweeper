mineField = [["X" for x in range(6)] for i in range(6)]
viewableField = [["X" for x in range(6)] for i in range(6)]
import random
game = True

class Mine():
    def __init__(self):
        pass
    
    def explode(self):
        print("END GAME. YOU STEPPED ON A MINE!")

def refresh():
    for i in range(len(viewableField[0])):
        print(viewableField[i])
    print("--------------------------------------")

def start():
    for i in range(4):
        mineField[random.randint(0,5)][random.randint(0,5)] = Mine()
    refresh()


def checkArond(row,col):
    nearby = 0
    if mineField[row][col] != "X":
        mineField[row][col].explode()
        viewableField[row][col] = "BOOM!"
        game = False
    try:
        mineField[row-1][col-1] != "X"
        nearby +=1
        viewableField[row][col] = str(nearby)
    except IndexError:
        nearby -=1
    try:    
        mineField[row-1][col] != "X"
        nearby += 1
        viewableField[row][col] = str(nearby)
    except IndexError:
        nearby -=1
    try:
        mineField[row-1][col+1] != "X"
        nearby +=1
        viewableField[row][col] = str(nearby)
    except IndexError:
        nearby -=1
    try:
        mineField[row][col-1] != "X"
        nearby +=1
        viewableField[row][col] = str(nearby)
    except IndexError:
        nearby -=1
    try:
        mineField[row][col+1] != "X"
        nearby +=1
        viewableField[row][col] = str(nearby)
    except IndexError:
        nearby -=1
    try:
        mineField[row+1][col-1] != "X"
        nearby +=1
        viewableField[row][col] = str(nearby)
    except IndexError:
        nearby -=1
    try:
        mineField[row+1][col] != "X"
        nearby +=1
        viewableField[row][col] = str(nearby)
    except IndexError:
        nearby -=1
    try:
        mineField[row+1][col+1] != "X"
        nearby +=1
        viewableField[row][col] = str(nearby)
    except IndexError:
        nearby -=1

    
def click(row,col):
    
    checkArond(row,col)
    
    refresh()

start()

while game:
    click(int(input("Row"))-1,int(input("Col"))-1)