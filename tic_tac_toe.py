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

drawField()

