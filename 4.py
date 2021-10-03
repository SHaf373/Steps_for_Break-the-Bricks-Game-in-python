import turtle
import random

win=turtle.Screen()
win.setup(width=800,height=600)
win.title('break the brakes')
win.bgcolor('black')

paddle=turtle.Turtle()
paddle.shape('square')
paddle.shapesize(stretch_wid=1,stretch_len=4)
paddle.color('white')
paddle.penup()
paddle.goto(0,-270)

ball=turtle.Turtle()
ball.shape('circle')
ball.color('brown')
ball.penup()
ball.dx=randomchoice((-5,-4,4,5))
ball.dy=randomchoice((-6,-5,-4,4,5,6))

pen=turtle.Turtle()
pen.color('white')
pen.up()
pen.hideturtle()
pen.goto(250,-220)
pen.write('SCORE:0',align='center',font=('Courier',24,'bold'))

colors = ['red', 'blue', 'green', 'cyan', 'purple', 'yellow', 'orange']
score = 0

def paddle_right():
    if paddle.xcor()<260:
        paddle.setx(paddle.xcor()+100)
def paddle_left():
    if paddle.xcor()>-260:
        paddle.setx(paddle.xcor()-100)
def paddle_up():
    if paddle.ycor()<260:
        paddle.sety(paddle.ycor()+100)

win.listen()
win.onkey(paddle_right,'Right')
win.onkey(paddle_left,'Left')
win.onkey(paddle_up,'Up')
