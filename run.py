# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random  # to use computer choice
import time  # to use sleep function
import os  # to use clear function
import sys
# choises : to store user and computer choises
# 9 item

playerName = ""
playerMark = "X"  # letter X or O
computerMark = "O"

gameCount = 0  # will max 3, if user want to start again
turnCount = 0  # will max 9, per game will reset
playerWinCount = 0  # will max 2, if user win 2 turn, user will win the game
currentPlayer = "player"  # player or computer

# table data
choises = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

# this function will switch player if current player is player, it will
# change to computer and vice versa

def switchPlayer():
    global currentPlayer
    if (currentPlayer == "player"):
        currentPlayer = "computer"
    else:
        currentPlayer = "player"

# this function will select first player randomly
def selectFirstPlayer():
    # we will use global variables
    global playerName
    global currentPlayer
    print("\n A draw is held to determine who will play first...\n")
    showLoading(1)
    # 1-10 random number
    random_number = random.randint(1, 10)
    # if random number is even, player will play first
    if (random_number % 2 == 0):
        print(f"\n\n {playerName} will play first !")
        currentPlayer = "player"
    else:
        print("\n\n Computer will play first !")
        currentPlayer = "computer"

# this function will get player name from user as input end return it
def getPlayerName():
    global playerName
    # this loop will continue until user enter a name
    while True:
        playerName = input("\n\n Enter your name: ")
        # strip function will remove spaces from start and end of string
        playerName = playerName.strip()
        # if user enter a name, it will return it

        # player name should be only letters
        if (not playerName.isalpha()):
            print("\n\n Please enter only letters !")
            continue
        if (len(playerName) > 0):
            return playerName
        else:  # if user enter empty string, it will continue loop
            print("\n\n Please enter your name !")

# this function will get player mark from user as input end return it
def getPlayerMark():
    # we will use global variables
    global playerMark
    global computerMark
    # this loop will continue until user enter valid a mark (X or O)
    while True:
        playerMark = input("\n\n Choose your mark (X or O): ")
        # strip function will remove spaces from start and end of string and
        # convert to uppercase to compare easily
        playerMark = playerMark.strip().upper()
        if (playerMark == "X" or playerMark == "O"):
            if (playerMark == "X"):
                computerMark = "O"
            else:
                computerMark = "X"
            return playerMark
        else:  # if user enter invalid mark, it will continue loop
            print("\n\n Please enter your mark !")

# this function will show loading animation from (I edited a little bit):
# https://medium.com/@joloiuy/creating-captivating-terminal-animations-in-python-a-fun-and-interactive-guide-2eeb2a6b25ec
def showLoading(seconds=1):
    animation = "|/-\\"
    start_time = time.time()
    while True:
        for i in range(4):
            time.sleep(0.2)  # Feel free to experiment with the speed here
            sys.stdout.write("\r\t" +
                             animation[i %
                                       len(animation)] +
                             "  -- Loading --  " +
                             animation[i %
                                       len(animation)])
            sys.stdout.flush()
            # The animation will last for 10 seconds
        if time.time() - start_time > seconds:
            break

# this function will get user choise from user as input end return it
def getUserChoise():
    # we will use global variables
    global userChoise
    # this loop will continue until user enter a valid choise
    while True:
        # get row and column from user and strip it
        # to remove spaces from start and end of string
        # and check if it is numeric or not
        row = input("\n\n Enter your row choise: ").strip()
        column = input("\n\n Enter your column choise: ").strip()
        # if its not numeric, it will continue loop
        if (not row.isnumeric()) or (not column.isnumeric()):
            print("\n\n Please enter a number !")
            continue
        else:  # if its numeric, it will convert to integer
            row = int(row)
            column = int(column)
            # if row or column is not between 1-3, it will continue loop
            if ((row < 1 or row > 3 or column < 1 or column > 3)):
                print("\n\n Please enter a number between 1-3 !")
                continue
            else:
                # if row and column is between 1-3
                # it will calculate the cell number and return it
                userChoise = ((int(row) - 1) * 3) + int(column)
                userChoise = int(userChoise)
                return userChoise
            
# this function will mark choise with player or computer mark and if
# choise is empty, it will return true, else false
def markChoise(choise):
    # we will use global variables
    global choises
    global currentPlayer
    # if choise is empty, mark it with player or computer mark
    if (choises[choise] == "-"):
        if (currentPlayer == "player"):
            choises[choise] = playerMark
        else:
            choises[choise] = computerMark
        return True
    else:
        print("\n\n This cell is not empty !")
        printTable()
        return False
    
# this function will print table 3x3
def printTable():
    print('''
            \n\t\t               columns
           \n\t\t            --↓---↓---↓----
          \n\t\t              1   2   3
          \n\t\t      |→ 1  | {} | {} | {} |
          \t   r  |     -------------
          \t   o  |→ 2  | {} | {} | {} |
          \t   w  |     -------------
         \t   s  |→ 3  | {} | {} | {} | \n'''.format(*choises))
    
# this function will check if player or computer win or not
def checkWin():
    # we will use
    global choises
    # check horizontal
    # line 1
    if (choises[0] == choises[1] and choises[1]
            == choises[2] and choises[0] != "-"):
        return choises[0]
    # line 2
    elif (choises[3] == choises[4] and
          choises[4] == choises[5] and
          choises[3] != "-"):
        return choises[3]
    # line 3
    elif (choises[6] == choises[7] and
          choises[7] == choises[8] and
          choises[6] != "-"):
        return choises[6]
    # check vertical
    # vertical line 1
    elif (choises[0] == choises[3] and
          choises[3] == choises[6] and
          choises[0] != "-"):
        return choises[0]
    # vertical line 2
    elif (choises[1] == choises[4] and
          choises[4] == choises[7] and
          choises[1] != "-"):
        return choises[1]
    # vertical line 3
    elif (choises[2] == choises[5] and
          choises[5] == choises[8] and
          choises[2] != "-"):
        return choises[2]
    # check diagonal
    # from left top to right bottom
    elif (choises[0] == choises[4] and
          choises[4] == choises[8] and
          choises[0] != "-"):
        return choises[0]
    # from right top to left bottom
    elif (choises[2] == choises[4] and
          choises[4] == choises[6] and
          choises[2] != "-"):
        return choises[2]
    else:
        # if no one win, it will return false
        return False
    
# this function will set table to initial state
def resetTable():
    global choises
    choises = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

# this function will check if table is full or not
def checkTableFull():
    # we will use global variables
    global choises
    # if there is a empty cell, it will return false
    for choise in choises:
        if (choise == "-"):
            return False
    # if there is no empty cell, it will return true
    return True

# this function will show score
def showScore():
    global gameCount
    global playerWinCount
    print(
        f"\n\n| {playerName} : {playerWinCount} " +
        f"| Computer : {gameCount-1 - playerWinCount} | ---  | \n\n")
    
# this function is main game play function
def playGame():
    # first of all, we will select first player
    selectFirstPlayer()
    # we will use global variables
    global gameCount
    global turnCount
    global currentPlayer
    global playerWinCount
    global playerName
    global playerMark
    # increase game count
    gameCount = gameCount + 1
    # print game is starting
    print(f"\n\n Game: {gameCount} is starting \n\n")
    # show loading animation
    showLoading(3)
    # clear the game result if there is for 2. or 3. game
    gameResult = ""  # win or lose
    # reset table if there is a game result for 2. or 3. game
    resetTable()
    # reset turn count for every game
    turnCount = 0
    # this loop will continue until game result is win, lose or tie
    while (gameResult == ""):
        # increase turn count for every turn
        turnCount = turnCount + 1
        # print who will play
        if (currentPlayer == "player"):
            print(f"\n\n {playerName} will play ! \n\n")
        else:
            print(f"\n\n {currentPlayer} will play ! \n\n")
        # print game table
        printTable()
        # get user choice until user enter a valid choise
        while True:
            print(f"\n\n Game: {gameCount} Turn: {turnCount}  \n\n")
            # show score
            showScore()
            # get the choise from user or computer. if current player is player
            # it will get from user, else it will get from computer
            # if current player is computer, it will get random number between
            # 1-9
            if (currentPlayer == "player"):
                choise = getUserChoise()
                print(f"\n\n {playerName} choised cell {choise} \n\n")
            else:
                choise = random.randint(1, 9)
                print(f"\n\n Computer choised cell {choise} \n\n")
            if (markChoise((choise - 1))):
                break
        # print game table after choise
        printTable()
        # check for win for every turn
        winner_mark = checkWin()
        # if there is a winner, print the winner and break the loop
        if (winner_mark):
            gameResult = "WON" if winner_mark == playerMark else "LOSE"
            print(f"\n\n {playerName} {gameResult} ! \n\n")
            if (gameResult == "WON" and winner_mark == playerMark):
                playerWinCount = playerWinCount + 1
            break
        # check for table full and if table is full
        # print tie and break the loop
        # this is a check for tie
        if (checkTableFull()):
            gameResult = "tie"
            print(f"\n\n Game is TIE ! \n\n")
            break
        # switch player for next turn
        switchPlayer()
        # show loading animation
        print("\n\n")
        showLoading(2)

# this function will initialize game
def initGame():
    # we will use global variables
    global playerName
    global gameCount
    print("\n\n Game is starting..\n\n")
    # show loading animation
    showLoading()

    # get the player name
    playerName = getPlayerName()
    print(f"\n\n Welcome {playerName} ! \n\n")
    showLoading()
    os.system("clear")
    print("\n\n You will play against computer. \n\n")
    # get the player mark (X or O)
    getPlayerMark()
    print("\n\n")
    showLoading(2)

    # play game until game count is 3
    while (gameCount < 3):
        playGame()
    # print game is over
    print("\n\n Game is over ! \n\n")
    # show score and print the winner
    print(
        f"\n\n| {playerName} : {playerWinCount} " +
        f"| Computer : {gameCount - playerWinCount} | ---  | \n\n")
    if (playerWinCount > gameCount - playerWinCount):
        print(f"\n\n {playerName} WON {playerWinCount} game(s) !!! \n\n")
    elif (playerWinCount < gameCount - playerWinCount):
        print(
            f"\n\n Computer WON {gameCount - playerWinCount} game(s) !!! \n\n")
    else:
        print(f"\n\n Game is tie ! \n\n")
    print("\n\n Thanks for playing ! \n\n")
    exitGame()


def showRules():
    # this function will show rules
    print("\n\n Tic Tac Toe Rules: \n\n")
    print(" 1) You will play against computer.")
    print(" 2) You will choose a number between 1-3.")
    print(" 3) You will try to complete a line.")
    print(" 4) If you complete a line, you will win the turn.")
    print(" 5) 3 game turn will play.")
    print(" 6) If you win minimum 2 turn, you will win the game.")


def exitGame():
    # this function will exit game
    print("\n\n Good Bye! See you soon... \n\n")
    exit()


def initMenu():
    # this function will initialize the menu
    menu_choise = input(
        " \n MENU \n 1) Rules \n " +
        "2) Start Game \n 3) Exit \n Enter your choise:")
    if (menu_choise == "1"):
        showRules()
        initMenu()
    elif (menu_choise == "2"):
        initGame()
    elif (menu_choise == "3"):
        exitGame()
    else:
        print("Wrong choise !")
        initMenu()

# main function is running at the beginning
def main():
    # clear terminal screen
    os.system("clear")
    print("""                     .-'''-.
                   '   _    \
                 /   /` '.   \
                .   |     \\  '
                |   '      |  '
   ____     ____\\    \\     / /____     _____
  `.   \\  .'    /`.   ` ..' /`.   \\  .'    /
    `.  `'    .'    '-...-'`   `.  `'    .'
      '.    .'                   '.    .'
      .'     `.                  .'     `.
    .'  .'`.   `.              .'  .'`.   `.
  .'   /    `.   `.          .'   /    `.   `.
 '----'       '----'        '----'       '----' """)
    print("\n\t WELCOME to TIC TAC TOE GAME !")
    initMenu()


main()
