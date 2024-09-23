# Falling One Object on Processing Python
 
Falling One Object Game 

Acknowledgments
Acknowledgments: This project was developed as an assignment for the Game Development 1 course (GAME 235) at the University of California, Santa Cruz. The code was developed with the help of Mohamed Samy and Mohamed-Ali-77. Additionally, we used ChatGPT to assist in structuring and refining parts of the project.

Overview
The is a simple game where a ball falls from the top of the screen, and the player moves a paddle to catch it. The game tracks the score, records failures, and increases the ball's speed as the score rises. Extra features include acceleration, a score display, and a high score tracking system.

Game Features
•	The falling object moves automatically, not controlled by the player.
•	The catching object moves based on player input, either through the mouse or keyboard.
•	Collision detection is implemented between the two objects, either by distance or rectangular checks depending on the visuals.
•	The falling object respawns at a random location when caught or when it falls off the screen.
•	A score is displayed during gameplay. 
•	A high score is displayed, which involves a fail state when the player misses. 
•	Acceleration or more interesting velocities are added to either object for a dynamic experience. 

Installation
1.	Download and install Processing.
2.	Enable Python Mode:
o	Open Processing.
o	Go to the Mode drop-down menu at the top right.
o	Select Python mode from the list.
3.	Clone or download this repository to your local machine.
4.	Open the falling_object_game.pde file in Processing.
Usage
1.	Launch Processing.
2.	Open the falling_object_game.pde file from this repository.
3.	Click the Run button in Processing to start the game.
4.	Use your mouse to control the paddle and catch the falling ball.

Example Code Snippet
```python
Copy code
ballPosX = 0  # start position of ball (position x) 
ballPosY = 0  # start position of ball (position Y) 
ballRadius = 20  # radius of the ball
ballFallSpeed = 5  # speed of the ball

paddlePosX = 0  # start position of paddle (position x) 
paddlePosY = 450  # start position of paddle (position y) 
paddleWidth = 50  # width of paddle
paddleHeight = 25  # height of paddle

score = 0  # start score
fail = 0  # start fail score

def setup():
    size(640, 480)  # background size
    background(255, 120, 120)  # background color
    noStroke()  # background without stroke
    textSize(32)  # text size
    rectMode(CENTER)  # set mode for drawing rectangles

def draw():
    global ballPosX, ballPosY, paddlePosX, score, fail, ballFallSpeed
    ballPosY += ballFallSpeed  # update ball position
    paddlePosX = mouseX  # control paddle with mouse

    # Ball falls off the screen
    if ballPosY > height + ballRadius:
        ballPosX = random(0, width)
        ballPosY = -ballRadius

    # Collision detection with paddle
    if ballPosX > paddlePosX - paddleWidth / 2 and ballPosX < paddlePosX + paddleWidth / 2:
        if ballPosY >= paddlePosY - paddleHeight / 2 and ballPosY <= paddlePosY + paddleHeight / 2:
            score += 1
            ballPosX = random(0, width)
            ballPosY = -ballRadius
            ballFallSpeed += 1  # increase speed after each catch

    # Failure case
    if ballPosY > height:
        fail += 1
        ballPosX = random(0, width)
        ballPosY = -ballRadius

    # Draw elements
    background(255, 120, 120)
    fill(120, 120, 255)  # ball color
    circle(ballPosX, ballPosY, ballRadius * 2)
    fill(220, 220, 220)  # paddle color
    rect(paddlePosX, paddlePosY, paddleWidth, paddleHeight)

    fill(35, 35, 35)  # text color
    text("Score: " + str(score), 10, 30)
    text("Fail: " + str(fail), 450, 30)

