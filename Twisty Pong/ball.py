from turtle import Turtle



class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
    
    """the move method sets the number of pixels the ball will move"""
    def move_right(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def move_left(self):
        new_x = self.xcor() + (self.x_move * -1)
        new_y = self.ycor() + (self.y_move * -1)
        self.goto(new_x, new_y)
    
    def bounce_y(self):
        self.y_move *= -1 #multiplying by -1 reverses the direction

    def bounce_x(self):
        self.x_move *= -1 #multiplying by -1 reverses the direction
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()