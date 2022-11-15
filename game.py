import random


class Mine():
    def __init__(self):
        pass
    
    def explode(self):
        print("END GAME. YOU STEPPED ON A MINE!")


class Grid():
    def __init__(self):
        self.rows = 6
        self.cols = 6
        self.mineField = [["X" for x in range(6)] for i in range(6)]
        self.viewableField = [["X" for x in range(6)] for i in range(6)]
        
        self.game = True
        
        for i in range(4):
            self.mineField[random.randint(0,5)][random.randint(0,5)] = Mine()

        
        while self.game == True:
            self.refresh()
            try:
                self.click(int(input("Row"))-1,int(input("Col"))-1)
            except:
                print("Wrong entry")

    def refresh(self):
        for i in range(len(self.viewableField[0])):
            print(self.viewableField[i])
        print("--------------------------------------")


    def checkArond(self,reqRow,reqCol):
        nearby = 0
        if self.mineField[reqRow][reqCol] != "X":
            self.mineField[reqRow][reqCol].explode()
            self.viewableField[reqRow][reqCol] = "BOOM!"
            self.game = False
        else:
            valid_rows = [reqRow]
            valid_cols = [reqCol]
            
            if 0 < reqRow < 5:
                valid_rows.append(reqRow - 1)
                valid_rows.append(reqRow + 1)
            elif reqRow == 0:
                valid_rows.append(reqRow + 1)
            elif reqRow == 5:
                valid_rows.append(reqRow - 1)
                
            if 0 < reqCol < 5:
                valid_cols.append(reqCol - 1) 
                valid_cols.append(reqCol + 1)
            elif reqCol == 0:
                valid_cols.append(reqCol + 1)
            elif reqCol == 5:
                valid_cols.append(reqCol -1)
            
            for R in valid_rows:
                for C in valid_cols:
                    if self.mineField[R][C] != "X":
                        nearby += 1
            
            self.viewableField[reqRow][reqCol] = str(nearby)

    
    def click(self,reqRow,reqCol):
        
        self.checkArond(reqRow,reqCol)
        

game = Grid()