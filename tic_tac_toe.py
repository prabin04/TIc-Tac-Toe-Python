#Creating Tic Tac Toe Game where we ask two users for input and user can put their cross or cirle  wherever they want.

# / / 
#-----
# / / 
#-----
# / / 
def drawField():
    for row in range(5):
        if row%2 == 0:
            for column in range(5):
                if column%2 == 0:
                    if column != 4:
                        print(" ", end = "")
                    else:
                        print(" ")
                else:
                    print("|", end ="")
        else:
            print("-----")
Player = 1
currentField = [[" "," "," "],[" "," "," "],[" "," "," "]]
while(True):
    MoveRow = int(input("Please enter the row: "))
    MoveColumn = int(input("Please enter the column: "))
    if Player == 1:
        #make move for player 1
        currentField[MoveColumn][MoveRow] = "X"
    else:
        #make move for player 2
        currentField[MoveColumn][MoveRow] = "O"


