import turtle
screen = turtle.Screen()
screen.screensize(800,800)
screen.bgcolor('lightsteelblue')




t_ground = turtle.Turtle() #groud
t = turtle.Turtle() #EVEYHTING




t.speed(10000000000000000000000000)


t_ground.speed(1000000000000000000000)
t_ground.pencolor('white')
t_ground.fillcolor("white")
t_ground.penup()
t_ground.goto(-1000,-100)
t_ground.pendown()
t_ground.begin_fill()
t_ground.goto(1000,-100)
t_ground.goto(1000,-1000)
t_ground.goto(1000,-1000)
t_ground.goto(-1000,-1000)
t_ground.end_fill()
t.penup()
t.goto(0,0)




t.pencolor("green")


#top tree
t.fillcolor("green")
t.begin_fill()
t.penup()
t.goto(0,50)
t.pendown()
t.goto(-40,10)
t.goto(40,10)
t.goto(0,50)
t.end_fill()
t.penup()


#second part
t.fillcolor("green")
t.begin_fill()
t.penup()
t.goto(0,25)
t.pendown()
t.goto(-60,-25)
t.goto(60,-25)
t.goto(0,25)
t.end_fill()
t.penup()


#third part
t.fillcolor("green")
t.begin_fill()
t.penup()
t.goto(0,0)
t.pendown()
t.goto(-80,-50)
t.goto(80,-50)
t.goto(0,0)
t.end_fill()
t.penup()


#fouth tree
t.fillcolor("green")
t.begin_fill()
t.penup()
t.goto(-80,-75)
t.pendown()
t.goto(0,-40)
t.goto(80,-75)
t.goto(-80,-75)
t.end_fill()
t.penup()




t.pencolor("brown")
t.fillcolor("brown")
t.begin_fill()
t.penup()
t.goto(-10,-75.50)
t.pendown()
t.goto(10,-75.50)
t.goto(10,-100)
t.goto(-10,-100)
t.goto(-10,-75.50)
t.end_fill()
t.penup()
t.goto(0,0)




#snowman body
t_ground.fillcolor('white')
t_ground.penup()
t_ground.begin_fill()
t_ground.goto(100,-100)
t_ground.pendown()
t_ground.circle(50)
t_ground.end_fill()
t_ground.penup()
t_ground.begin_fill()
t_ground.goto(100,-5)
t_ground.pendown()
t_ground.circle(35)
t_ground.end_fill()
t_ground.penup()
t_ground.begin_fill()
t_ground.goto(100,60)
t_ground.pendown()
t_ground.circle(25)
t_ground.end_fill()


#snowman eyes
t_ground.penup()
t_ground.pencolor('black')
t_ground.fillcolor('black')
t_ground.begin_fill()
t_ground.goto(90,90)
t_ground.circle(5)
t_ground.end_fill()
t_ground.penup()
t_ground.begin_fill()
t_ground.goto(110,90)
t_ground.circle(5)
t_ground.end_fill()
t_ground.penup()


#snowman nose
t_ground.goto(100,85)
t_ground.pencolor('orange')
t_ground.fillcolor('orange')
t_ground.pendown()
t_ground.begin_fill()
t_ground.goto(85,82)
t_ground.goto(100,75)
t_ground.goto(100,85)
t_ground.end_fill()
#snowman mouth
t_ground.penup()
t_ground.goto(100,66)
t_ground.pencolor('black')
t_ground.fillcolor('black')
t_ground.begin_fill()
t_ground.pendown()
t_ground.circle(2)
t_ground.end_fill()
t_ground.penup()
t_ground.begin_fill()
t_ground.goto(105,67)
t_ground.pendown()
t_ground.circle(2)
t_ground.end_fill()
t_ground.penup()
t_ground.begin_fill()
t_ground.goto(110,69)
t_ground.pendown()
t_ground.circle(2)
t_ground.end_fill()
t_ground.penup()
t_ground.begin_fill()
t_ground.goto(95,67)
t_ground.pendown()
t_ground.circle(2)
t_ground.end_fill()
t_ground.penup()
t_ground.begin_fill()
t_ground.goto(90,69)
t_ground.pendown()
t_ground.circle(2)
t_ground.end_fill()
t_ground.hideturtle()












t.pencolor('black')
t.fillcolor('red')
t.begin_fill()
t.speed (2)
t.penup()
t.goto(-100,-100)
t.pendown()
t.goto(-140,-100)
t.goto(-140,-55)
t.goto(-100,-55)
t.goto(-100,-55)
t.goto(-100,-100)
t.end_fill()
t.penup()




t.pencolor('black')
t.fillcolor('yellow')
t.begin_fill()
t.goto(-140,-75)
t.pendown()
t.goto(-100,-75)
t.goto(-100,-80)
t.goto(-140,-80)
t.goto(-140,-75)
t.end_fill()

def draw_square(color, size):
    t.fillcolor("red")
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.left(90)
        t.end_fill()

t.penup()
t.goto(-100,0)
t.pendown()


t.penup()
t.goto(100,0)
t.pendown()



t.hideturtle()
turtle.done()










#LAST LINE OF CODE
turtle.done()


