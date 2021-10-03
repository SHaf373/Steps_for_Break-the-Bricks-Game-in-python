import turtle
import random
import tkinter as tk
from tkinter import *

def tk():
    global namevalue
    root = Tk()
    root.title('GAME BY SHAF')
    photo = PhotoImage(file = "1.png")
    w = Label(root, image=photo)
    w.pack()

    label=Label(root,text='ENTER YOUR NAME:')
    label.pack()
    namevalue = StringVar()
    entry=Entry(root,textvariable=namevalue)
    entry.pack()
    button=Button(root,text='START GAME',bg="#FF5833",fg="#ecf0f1",command=main)
    button.pack()
    root.mainloop()
    

def main():
    n=namevalue.get()
    win = turtle.Screen()
    win.setup(width=800, height=600)
    win.bgcolor('brown')
    win.tracer(0)
    win.title('Break The Bricks')

    
    pen2=turtle.Turtle()
    pen2.color('black')
    pen2.up()
    pen2.hideturtle()
    pen2.goto(-250,-220)
    pen2.write(n, align='center', font=('Courier', 24, 'bold'))

    paddle=turtle.Turtle()
    paddle.shape("square")
    paddle.shapesize(stretch_len=5,stretch_wid=1)
    paddle.color("black")
    paddle.up()
    paddle.goto(0,-270)

    ball = turtle.Turtle()
    ball.shape('circle')
    ball.color('black')
    ball.up()
    ball.dx = random.choice((2,1,-2,-1)) #speed and direction
    ball.dy = random.choice((2,1,-2,-1))


    pen = turtle.Turtle()
    pen.color('black')
    pen.up()
    pen.hideturtle()
    pen.goto(250,-220)
    pen.write('Score: 0', align='center', font=('Courier', 24, 'bold'))


 
    colors = ['red', 'blue', 'green', 'cyan', 'purple', 'yellow', 'orange']
    score = 0


    def paddle_right():
        if paddle.xcor()<300:
            paddle.setx(paddle.xcor()+100)
    def paddle_left():
        if paddle.xcor()>-300:
            paddle.setx(paddle.xcor()-100)

    def border_check():
        if ball.ycor()>280:
            ball.dy *= -1
        if ball.xcor()>380 or ball.xcor()<-380:
            ball.dx *= -1
 
    def paddle_check():
        if ball.ycor() <= -250 and ball.ycor() >=-260 and ball.dy<0:
            if ball.xcor()-10 <= paddle.xcor() + 50 and ball.xcor() +10 >= paddle.xcor()-50:
                ball.dy *= -1
  


    win.listen()
    win.onkey(paddle_right, 'Right')
    win.onkey(paddle_left, 'Left')

    x_list = [-340, -230, -120, -10, 100, 210, 320]
    y_list = [280, 255, 230, 205, 180]
    block_list = []

    for i in y_list:
        for j in x_list:
            block = turtle.Turtle()
            block.shape('square')
            block.shapesize(stretch_len=5, stretch_wid=1)
            block.color(random.choice(colors))
            block.up()
            block.goto(j,i)
            block_list.append(block)
     
    block_count = len(block_list)

    while block_count>0:
        win.update()
        ball.goto(ball.xcor()+ball.dx, ball.ycor()+ball.dy)
        border_check()
        paddle_check()
        
     
        if ball.ycor() <-280:
            ball.goto(0,0)
            ball.dx *= -1
            pen.goto(0,0)
            pen.write(f'GAME OVER\nScore: {score} \n {n}', align='center', font=('Courier', 40, 'bold'))
            break
        

           
                
            

        
        # Block collisions:
        for i in block_list:
            if ball.xcor()+10 >= i.xcor()-50 and ball.xcor()-10 <= i.xcor()+50:
                if ball.ycor() >= i.ycor()-20 and ball.ycor() <= i.ycor()+20:
                    ball.dy *= -1
                    i.goto(1000,1000)
                    score += 1
                    block_count -= 1
                    pen.clear()
                    pen.write(f'Score: {score}', align='center', font=('Courier', 24, 'normal'))

tk()


