import turtle
import os

wn = turtle.Screen()
wn.title('Pong by Lord.Ace.369')
wn.bgcolor('maroon')
wn.setup(width=800,height=600)
wn.tracer(0)


# paddleA
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('blue')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# paddleB
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('green')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('yellow')
ball.penup()
ball.goto(0, 0)
ball.dx=2
ball.dy=2

# score
score_a=0
score_b=0

# pen
pen=turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,250)
pen.write(f'player A: {score_a}  player B: {score_b}',align='center',font=('courier',24,'normal'))


# Function
def paddle_a_up():
    y=paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)
def paddle_b_up():
    y=paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

#keyBoard Binding
wn.listen()
wn.onkeypress(paddle_a_up, 'w')
wn.onkeypress(paddle_a_down, 's')
wn.onkeypress(paddle_b_up, 'Up')
wn.onkeypress(paddle_b_down, 'Down')


# main game loop
game= True
while game == True:
    wn.update()

    # move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    # border checking
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1
        os.system("afplay bounce.wav&")
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy*=-1
        os.system("afplay bounce.wav&")

    #scoring    
    if ball.xcor()>390:
        os.system("afplay point.wav&")
        score_a+=1
        ball.goto(0,0)
        pen.clear()
        pen.write(f'player A: {score_a}  player B: {score_b}',align='center',font=('courier',24,'normal'))
    if ball.xcor()<-390:
        os.system("afplay point.wav&")
        score_b+=1
        ball.goto(0,0)
        pen.clear()
        pen.write(f'player A: {score_a}  player B: {score_b}',align='center',font=('courier',24,'normal'))
    
    # paddle bounce
    if (ball.xcor()==paddle_a.xcor()+10) and (ball.ycor()<=paddle_a.ycor()+50) and (ball.ycor()>=paddle_a.ycor()-50):
        ball.dx *= -1
        os.system("afplay bounce.wav&")
    if (ball.xcor()==paddle_b.xcor()-10) and (ball.ycor()<=paddle_b.ycor()+50) and (ball.ycor()>=paddle_b.ycor()-50):
        ball.dx *= -1
        os.system("afplay bounce.wav&")
    
    # winning score
    if score_a > 3 or score_b > 3:
        pen.clear()
        pen.write(f'Game over !',align='center',font=('courier',24,'normal'))
