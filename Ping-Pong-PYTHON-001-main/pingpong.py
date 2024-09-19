import turtle
import winsound

wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.setup(width=600, height=600)
wn.tracer(0)

#player A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("black")
# paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.shapesize(5, 1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#player B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("black")
# paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.shapesize(5, 1)
paddle_b.penup()
paddle_b.goto(350, 0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("black")
ball.penup()
ball.goto(0, 0)
ball.dx = 1
ball.dy = 1

#Score board
board = turtle.Turtle()
board.speed(0)
board.shape("square")
board.color("black")
board.penup()
board.hideturtle()
board.goto(0, 260)
board.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

#Score
score_a = 0
score_b = 0

#Paddle A
def paddle_a_up():
    y = paddle_a.ycor()
    y += 40
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 40
    paddle_a.sety(y)

#Paddle B
def paddle_b_up():
    y = paddle_b.ycor()
    y += 40
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 40
    paddle_b.sety(y)

#keys for Player A
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")

#keys for Player B
wn.onkeypress(paddle_b_up, "a")
wn.onkeypress(paddle_b_down, "d")

# game loop
while True:
    wn.update()
    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border checking top and bottom
    if ball.ycor() > 290:
        # ball.sety(290)
        ball.dy *= -1

    elif ball.ycor() < -290:
        # ball.sety(-290)
        ball.dy *= -1

    #paddle and ball collisions left and right
    if ball.xcor() > 350:
        # ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        board.clear()
        board.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound("SystemQuestion", winsound.SND_ASYNC)

    elif ball.xcor() < -350:
        # ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        board.clear()
        board.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound("SystemQuestion", winsound.SND_ASYNC)

    #return
    if ball.xcor()<-340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1
        winsound.Beep(500,50)

    elif ball.xcor()>340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1
        winsound.Beep(500,50)

# turtle.done()