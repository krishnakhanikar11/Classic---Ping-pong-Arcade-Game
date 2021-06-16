import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Ping-Pong Game')
screen.tracer(0)

line = Turtle()
line.hideturtle()
line.color('white')
line.penup()
line.goto(0, 300)
line.setheading(270)
for i in range(16):
    line.speed('fastest')
    line.pendown()
    line.forward(20)
    line.penup()
    line.forward(20)

paddleA = Paddle((-350, 0))
paddleB = Paddle((350, 0))
ball = Ball()
scoreA = Score((-100, 200))
scoreB = Score((100, 200))

screen.listen()
screen.onkey(paddleA.up, "Up")
screen.onkey(paddleA.down, "Down")
screen.onkey(paddleB.up, "w")
screen.onkey(paddleB.down, "s")

is_game_on = True

while is_game_on:

    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(paddleB) < 50 and ball.xcor() > 340:
        ball.bounce_x()

    if ball.distance(paddleA) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    if ball.xcor() < -380:
        scoreB.update_B()
        ball.re()
        ball.bounce_x()

    if  ball.xcor() > 380:
        scoreA.update_A()
        ball.re()
        ball.bounce_x()

screen.exitonclick()
