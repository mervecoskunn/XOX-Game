# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random  #to use computer choice
import time  #to use sleep function
import os  #to use clear function
import sys
# choises : to store user and computer choises
# 9 item

playerName = ""
playerMark = "X"  #letter X or O
computerMark = "O"

gameCount = 0  # will max 3, if user want to start again
turnCount = 0  # will max 9, per game will reset
playerWinCount = 0  # will max 2, if user win 2 turn, user will win the game
currentPlayer = "player"  # player or computer

#table data
choises = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

def switchPlayer():
    global currentPlayer
    if(currentPlayer == "player"):
        currentPlayer = "computer"
    else:
        currentPlayer = "player"
def selectFirstPlayer():
    print("\n A draw is held to determine who will play first...\n")
    showLoading(1)
    random_number = random.randint(1, 10)
    if(random_number % 2 == 0):
        print(f"\n\n {playerName} will play first !")
        currentPlayer = "player"
    else:
        print("\n\n Computer will play first !")
        currentPlayer = "computer"
def getPlayerName():
    while True:
        playerName = input("\n\n Enter your name: ")
        playerName = playerName.strip()
        if(len(playerName) > 0):
            return playerName
        else:
            print("\n\n Please enter your name !")
def getPlayerMark():
    while True:
        playerMark = input("\n\n Choose your mark (X or O): ")
        playerMark = playerMark.strip()
        if(playerMark == "X" or playerMark == "O"):
            return playerMark
        else:
            print("\n\n Please enter your mark !")
def showLoading(seconds=1):
    animation = "|/-\\"
    start_time = time.time()
    while True:
        for i in range(4):
            time.sleep(0.2)  # Feel free to experiment with the speed here
            sys.stdout.write("\r\t"+animation[i % len(animation)]+"  -- Loading --  " + animation[i % len(animation)])
            sys.stdout.flush()
        if time.time() - start_time > seconds:  # The animation will last for 10 seconds
            break

def getUserChoise():
    while True:
        userChoise = input("\n\n Enter your choise: ")
        userChoise = userChoise.strip()
        if(userChoise.isnumeric()):
            userChoise = int(userChoise)
            if(userChoise > 0 and userChoise < 10):
                return userChoise
            else:
                print("\n\n Please enter a number between 1-9 !")
        else:
            print("\n\n Please enter a number !")

def markChoise(choise):
    ## if choise is empty, mark it with player or computer mark
    if(choises[choise] == "-"):
        if(currentPlayer == "player"):
            choises[choise] = playerMark
        else:
            choises[choise] = computerMark
        return True
    else:
        print("\n\n This choise is not empty !")
        printTable()
        return False

def printTable():
    print(''' \n\t\t | {} | {} | {} | \n\t\t ------------- \n\t\t | {} | {} | {} | \n\t\t -------------  \n\t\t | {} | {} | {} | '''.format(*choises))

def checkWin():
    ## check horizontal
    if(choises[0] == choises[1] and choises[1] == choises[2] and choises[0] != "-"):
        return choises[0]
    elif(choises[3] == choises[4] and choises[4] == choises[5] and choises[3] != "-"):
        return choises[3]
    elif(choises[6] == choises[7] and choises[7] == choises[8] and choises[6] != "-"):
        return choises[6]
    ## check vertical
    elif(choises[0] == choises[3] and choises[3] == choises[6] and choises[0] != "-"):
        return choises[0]
    elif(choises[1] == choises[4] and choises[4] == choises[7] and choises[1] != "-"):
        return choises[1]
    elif(choises[2] == choises[5] and choises[5] == choises[8] and choises[2] != "-"):
        return choises[2]
    ## check diagonal
    elif(choises[0] == choises[4] and choises[4] == choises[8] and choises[0] != "-"):
        return choises[0]
    elif(choises[2] == choises[4] and choises[4] == choises[6] and choises[2] != "-"):
        return choises[2]
    else:
        return False

def playGame():
    global gameCount
    global turnCount
    global currentPlayer
    global playerName
    gameCount = gameCount + 1
    gameResult = "" ## win or lose

    while(gameResult ==""):
        turnCount = turnCount + 1
        ## pring game and turn count
        print(f"\n\n Game: {gameCount} Turn: {turnCount} \n\n")
        ## pring who will play
        if(currentPlayer == "player"):
            print(f"\n\n {playerName} will play ! \n\n")
        else:
            print(f"\n\n {currentPlayer} will play ! \n\n")
        ## print table
        printTable()
        ## get user choice
        while True:
            choise = getUserChoise() if currentPlayer == "player" else random.randint(1, 10)
            if(markChoise(choise-1)):
                break
            ## check for win
        winner_mark = checkWin()
        if(winner_mark != False):
            gameResult = "win" if winner_mark == playerMark else "lose"
            printTable()
            print(f"\n\n {playerName} {gameResult} ! \n\n")
            break
        switchPlayer()    

        showLoading(0.2)
        os.system("clear")


def initGame():
    print ("\n\n Game is starting..\n\n")
    showLoading()
    os.system("clear") ## clear terminal screen
    playerName = getPlayerName()
    print(f"\n\n Welcome {playerName} ! \n\n")
    showLoading() ## wait 1 second
    os.system("clear") ## clear terminal screen
    print("\n\n You will play against computer. \n\n")
    getPlayerMark()
    showLoading(2) ## wait 0.5 second
    os.system("clear") ## clear terminal screen
    selectFirstPlayer()
    playGame()



def showRules():
    print("\n\n Tic Tac Toe Rules: \n\n")
    print(" 1) You will play against computer.")
    print(" 2) You will choose a number between 1-9.")
    print(" 3) You will try to complete a line.")
    print(" 4) If you complete a line, you will win the turn.")
    print(" 5) 3 game turn will play.")
    print(" 6) If you win minimum 2 turn, you will win the game.")

def exitGame():
    print("\n\n Good Bye ! \n\n")
    exit()

def initMenu():
    menu_choise = input("\n 1) Rules: \n 2) Start Game: \n 3) Exit \n Enter your choise:")
    if(menu_choise == "1"):
        showRules()
        initMenu()
    elif(menu_choise == "2"):
        initGame()
    elif(menu_choise == "3"):
        exitGame()
    else:
        print("Wrong choise !")
        initMenu()
  
print("""                     .-'''-.                     
                   '   _    \                   
                 /   /` '.   \                  
                .   |     \  '                  
                |   '      |  '                 
   ____     ____\    \     / /____     _____    
  `.   \  .'    /`.   ` ..' /`.   \  .'    /    
    `.  `'    .'    '-...-'`   `.  `'    .'     
      '.    .'                   '.    .'       
      .'     `.                  .'     `.      
    .'  .'`.   `.              .'  .'`.   `.    
  .'   /    `.   `.          .'   /    `.   `.  
 '----'       '----'        '----'       '----' """)
print("\nWelcome to Tic Tac Toe Game !")

initMenu()
