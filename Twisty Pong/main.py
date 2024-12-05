from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen() #this pops up a blanck screen
screen.setup(width=800, height=600) #screen size
screen.bgcolor("black") #screen color
screen.title("Pong Twist") #screen title
screen.tracer(0) #the tracer method freezes the screen so that an animation is not seen. Instead we see the final position of the object.

r_paddle = Paddle((350, 0)) #this uses the Paddle class to create an object and is positioned on the right side
l_paddle = Paddle((-350, 0)) #same as above but left side
ball = Ball() #this uses the Ball class to create the ball object. The attributes are set out in the init method
scoreboard = Scoreboard() #this uses the Scoreboard class to create and position the scoreboard on the top of the window


screen.listen() #this method allows for user keys input
screen.onkey(r_paddle.go_up, "Up") #onkey is a Screen class method. Here we define the object impacted by the action and the argument which is the Up key
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed) #this defines the speed of the ball
    screen.update()
    ball.move_right()
    
    #detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    #detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #detect collision with edge
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    
    elif ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        

        


    
screen.exitonclick()