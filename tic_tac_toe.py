#Creating Tic Tac Toe Game where we ask two users for input and user can put their cross or cirle  wherever they want.

# / / 
#-----
# / / 
#-----
# / / 
def drawField(field):
    for row in range(5):  #0,1,2,3,4
                          #0,.,1,.,2
        # if row is even row write " | |  "
        if row%2 == 0:
            practicalRow = int(row/2)
            for column in range(5):  # will take values 0 (in drawing) -> 0 (in actual field), 1->., 2->1, 3->., 4->2
                # if column is even, we will print a space
                # The even columns gives us the move of each player
                if column%2 == 0: # Values 0,2,4
                    # The actual column that should be used in our field
                    # Make sure our values are integers
                    practicalColumn = int(column/2)  # Values 0,1,2
                    if column != 4:
                        # Print the specific field
                        print(field[practicalColumn][practicalRow],end="") # Continue in the same line
                    else:
                        print(field[practicalColumn][practicalRow]) # Jump to the next line
                else:
                    # The odd value just give us vertical lines
                    print("|",end="")
        else:
            print("-----")


# Create a variable for the Players
Player = 1

currentField = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]] # A list that contains 3 lists

# We will draw the current field
drawField(currentField)

# Create an infinite loop for the gamez
while(True): # True == True / is always true (We can also use while(1))
    # Display the player's turn
    print("Players turn: ",Player)
    # Ask user for input: to specify the desired row and column
    MoveRow = int(input("Please enter the row\n"))       # Convert the row to integer
    MoveColumn = int(input("Please enter the column\n")) # Convert the column to integer
    if Player == 1:
        # Make move for player 1
        # Access our current field
        # We only want to make one move when that specific field is empty
        if currentField[MoveColumn][MoveRow] == " ":
            currentField[MoveColumn][MoveRow] = "X"
            # Once Player 1 make his move we change the Player to 2
            Player = 2
    else:
        # Make move for player 2
        if currentField[MoveColumn][MoveRow] == " ":
            currentField[MoveColumn][MoveRow] = "O"
            Player = 1

    # At the end, draw the current field representation
    drawField(currentField)
