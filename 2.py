import turtle 
win=turtle.Screen()
win.setup(width=800,height=600)
win.bgcolor('black')

paddle=turtle.Turtle()
paddle.shape('square')
paddle.shapesize(stretch_len=5,stretch_wid=1)
paddle.color('white')
paddle.penup()
paddle.goto(0,-270)


def paddle_right():
    if paddle.xcor()<260:
        paddle.setx(paddle.xcor()+100)
def paddle_left():
    if paddle.xcor()>-260:
        paddle.setx(paddle.xcor()-100)
win.listen()
win.onkey(paddle_right,'Right')
win.onkey(paddle_left,'Left')

