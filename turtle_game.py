import turtle
import random

wn = turtle.Screen()
wn.title("Simple Turtle Graphing Game")
wn.setup(width = 900, height = 900)
wn.bgcolor("black")
wn.tracer(0)

class Player(turtle.Turtle): 
    def __init__(self, color): 
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(10)
        self.color(color)
        self.shape("turtle") 
        self.lives = 0
        self.speed = 3
        self.score = 0

    def move(self): 
        self.fd(self.speed)

        if self.xcor() > 390:
            self.setx(390)
            self.rt(60)
        if self.ycor() > 390:
            self.sety(390)
            self.rt(60)
        if self.xcor() < -390:
            self.setx(-390)
            self.rt(60)
        if self.ycor() < -390:
            self.sety(-390)
            self.rt(60)
        
        for object in objects:
            if self.distance(object) < 20: 
                object.jump()
            if isinstance(object, Obstacle): 
                self.score -= 1
            elif isinstance(object, Goal):
                self.score += 1 
    
    def turn_left(self): 
        self.lt(30)
        
    def turn_right(self): 
        self.rt(30)

    def accelerate(self): 
        self.speed += 1

    def decelerate(self): 
        self.speed -= 1


class Goal(turtle.Turtle): 
    def __init__(self, color): 
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.color(color)
        self.shape("circle") 
        self.lives = 0
        heading = random.randint(0,360)
        self.setheading(heading)

    def move(self): 
        self.fd(3)
        if self.xcor() > 390:
            self.setx(390)
            self.rt(60)
        if self.ycor() > 390:
            self.sety(390)
            self.rt(60)
        if self.xcor() < -390:
            self.setx(-390)
            self.rt(60)
        if self.ycor() < -390:
            self.sety(-390)
            self.rt(60)

    def jump(self):
         x = random.randint(-390, 390)
         y = random.randint(-390, 390)
         self.goto(x,y)


class Obstacle(Goal): 
    def __init__(self, color): 
        Goal.__init__(self, color)
        self.color = color


objects = []
for i in range(10):
    goal = Goal("blue")
    goal.jump()
    objects.append(goal)

    obstacle = Obstacle("red")
    obstacle.jump()
    objects.append(obstacle)


player = Player("Blue")

goal.goto(100,0)

wn.listen()
wn.onkeypress(player.accelerate, "Up")
wn.onkeypress(player.decelerate, "Down")
wn.onkeypress(player.turn_right, "Right")
wn.onkeypress(player.turn_left, "Left")


while True: 
    wn.update()
    player.move()
    
    for object in objects:
        object.move()


wn.mainloop()