import turtle 
import random 

wn = turtle.Screen() 
wn.title("Bouncing Value Simulation") 
wn.bgcolor("black") 

wn.tracer(0) 

colors = ["red", "green", "blue", "orange", "yellow"]
balls = []

for _ in range(15): 
    ball = turtle.Turtle()
    ball.shape("circle") 
    color = random.choice(colors)
    ball.color(color)
    ball.penup() 
    ball.speed(0)
    x = random.randint(-250, 250)
    y = random.randint(250, 400)
    ball.goto(x, y)  
    ball.dy = 0 
    ball.dx = 1 
    balls.append(ball)

GRAVITY = -0.1 


while True: 
    wn.update()
    
    for ball in balls: 
        ball.dy += GRAVITY 

        x = ball.xcor()
        x += ball.dx 
        y = ball.ycor() 
        y += ball.dy 
        ball.goto(x,y) 
    
        if ball.ycor() < -250:
            ball.dy *= -1
        
        if ball.xcor() > 250: 
            ball.dx *= -1 
        if ball.xcor() < -250: 
            ball.dx *= -1 
     
wn.mainloop()