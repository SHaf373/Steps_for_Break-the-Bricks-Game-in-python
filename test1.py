import turtle

screen=turtle.Screen()
screen.setup(width=800,height=600)
screen.bgcolor=("black")
screen.title("break the bricks")


paddle=turtle.Turtle()
paddle.shape=("square")
paddle.shapesize(stretch_len=5,stretch_wid=1)
paddle.color=("white")
paddle.penup()
paddle.goto(0,-270)
