from turtle import Screen
from paddles import Paddle
from ball import  Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle_right = Paddle((350,0))
paddle_left = Paddle((-350,0))
scoreboard = Scoreboard()

ball = Ball()


screen.listen()
screen.onkey(paddle_right.go_up, "Up")
screen.onkey(paddle_right.go_down, "Down")

screen.onkey(paddle_left.go_up, "w")
screen.onkey(paddle_left.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.acceleration)
    screen.update()
    ball.move()

    #Collision with paddle_left
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        ball.accelerate()

    #Collision with paddle_right
    if ball.distance(paddle_right) < 50 and ball.xcor() > 320 or ball.distance(paddle_left) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        scoreboard.update()
        ball.accelerate()


    if ball.xcor() > 380:
        time.sleep(2)
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -390:
        time.sleep(2)
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()