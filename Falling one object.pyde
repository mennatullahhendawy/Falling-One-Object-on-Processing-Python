

ballPosX = 0 #start position of ball (position x) 
ballPosY = 0 #start position of ball (position Y) 
ballRadius = 20 #radius of the ball
ballFallSpeed = 5 #speed of the ball

paddlePosX = 0 #start position of paddle (position x) 
paddlePosY = 450 #start position of paddle (position y) 
paddleWidth = 50 #width of paddle
paddleHeight = 25 #height of paddle

score = 0 #start score
fail = 0  #start score for failure attempts

def setup():
    size (640,480) #background size
    background (255, 120, 120) #background color
    noStroke() #background without a stroke
    textSize(32) # text size for "fail" and "start
    rectMode(CENTER) #mouse location
    
    global ballPosX, ballPosY #real-time variables
    ballPosX = width/2 #start position of the ball in the middle of the screen / background
    ballPosY = -ballRadius #falling of the ball
    
def draw(): #fuction to draw
    global ballPosX, ballPosY, paddlePosX, score,fail, ballFallSpeed #variables that wil change real-time
    ballPosY =ballPosY + ballFallSpeed #ball repeated movement
    paddlePosX = mouseX #paddle moving with the mouse in X direction
    
    if ballPosY > height +ballRadius: #if statement if the start position for the ball
        ballPosX = random (0,width)#randomn start for the ball
        ballPosY = -ballRadius #falling of the ball
        
    if ballPosX > paddlePosX - paddleWidth/2 and ballPosX < paddlePosX + paddleWidth/2: #collision if statement when the ball is inbetween in relation to paddle X and Y position
        if ballPosY >= paddlePosY - paddleHeight/2 and ballPosY <= paddlePosY + paddleHeight/2: #check if ball touches paddle
            score = score +1 #increase of score in case of collision 
            ballPosX = random (0,width) #initialize a new start for the ball falling
            ballPosY = -ballRadius #initialize of y position
            ballFallSpeed=ballFallSpeed+1#increasing the ball speed after every success


    if ballPosY> height: #condition for the failure case
        fail = fail + 1 #increase fail score +1
        ballPosX = random (0,width)  #initialize a new start for the ball falling
        ballPosY = -4 #initialize a new position u (it has to be any number less than height) 




    background (255, 120, 120) #screen color
   
    fill (120, 120, 255) #circle color (ball color)
    circle (ballPosX, ballPosY, ballRadius*2) #position and radius of the ball
    
    fill (220, 220, 220) #paddle 
    rect (paddlePosX, paddlePosY, paddleWidth, paddleHeight) #position and size of the paddle
    
    fill (35,35,35) #text color
    text ("Score:" +str (score), 10, 30) #score text position
    text ("fail:" + str(fail), 450, 30) #fail text position
