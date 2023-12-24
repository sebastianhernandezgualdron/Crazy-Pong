import os
import turtle as t
playerOneScore = 0
playerTwoScore = 0
speedIncrement = 0.001


window=t.Screen()
window.title("PrimerPong")
window.bgpic("imgs/pngtree-2d-landscape-of-nature-theme-at-night-time-picture-image_1172538.png")
window.setup(width=800,height=600)
window.tracer(0)


leftPaddle = t.Turtle()
leftPaddle.speed(0)
leftPaddle.shape("square")
leftPaddle.color("white")
leftPaddle.shapesize(stretch_wid=5, stretch_len=1)
leftPaddle.penup()
leftPaddle.goto(-350,0)

RightPaddle=t.Turtle()
RightPaddle.speed(0)
RightPaddle.shape("square")
RightPaddle.color("white")
RightPaddle.shapesize(stretch_wid=5, stretch_len=1)
RightPaddle.penup()
RightPaddle.goto(350,0)

ballPaddle = t.Turtle()
ballPaddle.speed(3)
ballPaddle.shape("circle")
ballPaddle.color("red")
ballPaddle.penup()
ballPaddle.goto(5,5)
ballXdirection = 0.2
ballYdirection = 0.2


pen = t.Turtle()
pen.speed(0)
pen.color("Red")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("score", align="center", font=("Arial", 24, "normal"))


def leftPaddleUp():
    y=leftPaddle.ycor()
    y = y+30
    leftPaddle.sety(y)

def leftPaddleDown():
    y=leftPaddle.ycor()
    y = y-30
    leftPaddle.sety(y)

def RightPaddleUp():
    y=RightPaddle.ycor()
    y = y+30
    RightPaddle.sety(y)

def RightPaddleDown():
    y=RightPaddle.ycor()
    y = y-30
    RightPaddle.sety(y)


window.listen()
window.onkeypress(leftPaddleUp, "w")
window.onkeypress(leftPaddleDown, "s")
window.onkeypress(RightPaddleUp, "Up")
window.onkeypress(RightPaddleDown, "Down")

while True:

    window.update()
    ballYdirection = ballYdirection + speedIncrement
    ballXdirection = ballXdirection + speedIncrement

    ballPaddle.setx(ballPaddle.xcor()+ballXdirection)
    ballPaddle.sety(ballPaddle.ycor()+ballYdirection)

    if ballPaddle.ycor()>290:
        ballPaddle.sety(290)
        ballYdirection = ballYdirection*-1
    if ballPaddle.ycor()<-290:
        ballPaddle.sety(-290)
        ballYdirection=ballYdirection*-1

    if ballPaddle.xcor() >390:
        ballPaddle.goto(0,0)
        ballXdirection = ballXdirection * -1
        playerOneScore = playerOneScore + 1
        pen.clear()
        pen.write("Player One: {}     Player B: {}".format(playerOneScore,playerTwoScore), align="center", font=("Monaco",24,"normal"))
        os.system("afplay wallhit.wav&")

    if ballPaddle.xcor() < -390:
        ballPaddle.goto(0,0)
        ballXdirection = ballXdirection * -1
        playerTwoScore = playerTwoScore + 1
        pen.clear()
        pen.write("Player One: {}     Player B: {}".format(playerOneScore,playerTwoScore), align="center", font=("Monaco",24,"normal"))
        os.system("afplay wallhit.wav&")

    if(ballPaddle.xcor()>340) and (ballPaddle.xcor() < 350) and (ballPaddle.ycor() < RightPaddle.ycor() + 40 and ballPaddle.ycor() > RightPaddle.ycor() - 40):
        ballPaddle.setx(340)
        ballXdirection = ballXdirection * -1

        os.system("asplay paddle.wav&")

    if(ballPaddle.xcor()< -340) and (ballPaddle.xcor() > - 350) and (ballPaddle.ycor() < leftPaddle.ycor() + 40 and ballPaddle.ycor() > leftPaddle.ycor() - 40):
        ballPaddle.setx(-340)
      
        ballXdirection = ballXdirection * -1
        os.system("asplay paddle.wav&")

