 # XOX-GAME
 [XOX-GAME](https://tic-tac-toe-game-merve-f793c47a141b.herokuapp.com/) This project is a game project. It is a popular game also known as tic-tac-toe-game. XOX-GAME is run and played within the terminal. The system runs on a mock terminal through [Heroku](https://id.heroku.com/login) It is a game that can be played 3 times between the computer and one player and results in winning, drawing or losing.
 Click here to play the game: [XOX-GAME](https://tic-tac-toe-game-merve-f793c47a141b.herokuapp.com/)

 ![Am I Responsive?](images/XOX-GAME-responsive.png)

## How to Play

![Start Screen](images/start-screen.png)

When we click on the live link [XOX-GAME](https://tic-tac-toe-game-merve-f793c47a141b.herokuapp.com/) to start the game, we are greeted with this start screen. We see a menu that will help guide us, and we proceed by typing a number between 1 and 3 to select the option we want.

 ### If we choose 1 from the menu

 ![select-1](images/Select-1.png)

If we choose 1. The rules tab will open and we can see the rules of the game as shown in the picture above.

### If we choose 2 from the menu

 ![select-2](images/select-2.png)

If we choose 2, the game will start and ask us to enter a username. If an invalid character is entered, we will see a warning message on this screen.

![message-invalid-username](images/select-2-1.png)

### If we choose 3 from the menu

![select-3](images/select-3.png)

If 3 is selected from the menu, you will be exited and this screen will be seen.

## Features

### Existing Features

After entering the username, the next step is to start the game and a choice is made between X and O(we use letter O, it is not a number)
![choose-mark](images/choose-mark.png)

After the sign is selected, the computer and the user randomly choose who will start playing first and the game begins.

Then, who will play first is written on the screen, and if the player is selected to make the first move, after the initial score information is given, player is asked for information on which cell player will tick on the game board and the choice is made.

#### for row:

![first-step](images/first-step.png)

#### for column:

![first-step-1](images/first-step-1.png)

After the choice is made, we can see the sign placed on the game board.

![merve-first](images/merve-first.png)

If the computer is going to play first, a message is given that the computer will play, then the move is passed to the other player.

![computer-first](images/computer-first.png)

If the player wants to re-select a previously selected location, player will encounter a warning like the one in the picture below.

![not-empty](images/not-empty.png)


## Technologies Used

  * [Github](https://github.com/)- The site was used to edit and host the website.
  * [GitPod](https://gitpod.io/projects)- Used in the deployment and creating the website.
  * [Python](https://www.python.org/)- This was used in the production to get the game running as it is required for the app to run.
  * [Node.js](https://nodejs.org/en/) - This was used in the production to get the game running as it is required for app to run.
  * [pep8online]()- This site was used to validate the python code to check for any errors within my writing.
  * [Heroku](https://id.heroku.com/login)- This was used to deploy the game in a mock terminal that allows anyone to play the game online.
  * [ASCII ART](https://patorjk.com/software/taag/#p=display&f=JS%20Bracket%20Letters&t=XOX)- We used this as the logo when starting the game.(Font name: Crazy)
  * [Animation](https://medium.com/@joloiuy/creating-captivating-terminal-animations-in-python-a-fun-and-interactive-guide-2eeb2a6b25ec)- We used this to animate the Python terminal loading source code.

## Deployment

### Deployment of the project

I deployed this project with [Heroku](https://id.heroku.com/login), a cloud platform, using the credits provided by [Code Institute](https://codeinstitute.net/se/) to our students.

To deploy this project I used the following steps in Heroku:
  * Fork or clone a copy of this repository.
  * Log in or create an account in heroku.
  * Click on the button in the right corner to create a new app.
  * Inside the app page, go to setting page (underlined in green) and set the buildpacks to "Python" and "Nodejs" in that order (like in the picture below).
  * Link the heroku app to the repository.
  * Go back to the deploy page (underlined in yellow) and you can either choose to manually deploy the site or automatically.
  * Once it has deployed, it may take a fww minutes to load and you can play the game.
  * The link to the page to play the game can be found here - [XOX-GAME](https://tic-tac-toe-game-merve-f793c47a141b.herokuapp.com/)


  ### Cloning of the Project

  To create a local clone of the project, follow the steps below:
    1. In the GitHub repository, under the repository name there is a code tab., click on the code tab.
    2. In the clone tab, click the HTTPS tab. Within this section, click on the clipboard icon and copy the URL supplied for the repository.
    3. Open an IDE of your choosing and run Git Bash.
    4. Change the current working directory to the location of which you wish to place the cloned repository.
    5. In the terminal, write Git Clone and then paste in the URL supplied via GitHub from step 2.
    6. Press enter and your new cloned repository will be created within the desired location.
  ## Credits 
    1. [ASCII ART](https://patorjk.com/software/taag/#p=display&f=JS%20Bracket%20Letters&t=XOX)- We used this as the logo when starting the game.(Font name: Crazy).
    2. [Animation](https://medium.com/@joloiuy/creating-captivating-terminal-animations-in-python-a-fun-and-interactive-guide-2eeb2a6b25ec)- We used this to animate the Python terminal loading source code.

## Acknowledgements

This project is my 3rd Portfolio Project for the Full Stack Software Developer (e-Commerce) Diploma course provided by the [Code Institute](https://codeinstitute.net/se/).
I would like to thank my mentor [Precious ljege](https://www.linkedin.com/in/precious-ijege-908a00168/) who helped me while developing my project.


