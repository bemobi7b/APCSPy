import turtle

tort = turtle.Turtle()
tort.speed(0)
tort.penup()

tx = 100
ty = 100

tort.pencolor("Red")
tort.color("Blue")

tort.goto(-100,100)
tort.pendown()
tort.pensize(3)
tort.goto(-100,60)
tort.goto(-120,80)
tort.goto(-120,115)
tort.goto(-110,130)
tort.goto(-100,115)
tort.goto(-100,100)
tort.pendown()
tort.pensize(1)
tort.goto(100,100)
tort.pensize(3)
tort.goto(100,60)
tort.goto(120,80)
tort.goto(120,115)
tort.goto(110,130)
tort.goto(100,115)
tort.goto(100,100)
tort.pensize(1)

def ttt():
    tort.goto(tx,ty)
    


for n in range(10):
    tx -= 10
    tort.goto(tx,110)
    tx -= 10
    tort.goto(tx,100)

for n in range(10):
    tort.penup()
    tx = -100
    ty = 100 - (10 * (n))
    ttt()
    tort.pendown()
    for n in range(20):
        ty -= 10
        ttt()
        tx += 10
        ttt()
        ty += 10
        ttt()

tort.penup()
tort.goto(40,0)
tort.pendown()


def talloval(r):               
    tort.left(90)
    # for loop in range(2):      # Draws 2 halves of ellipse
    tort.circle(r,45)    # Long curved part
    tort.circle(r/2,90)
    tort.circle(r,45)  


tort.fillcolor("white")
tort.begin_fill()
talloval(60)
tort.goto(40,0)
tort.end_fill()
    
tort.penup()
tort.goto(-10,0)
tort.pendown()
tort.goto(0,15)
tort.goto(10,0)
tort.goto(0,15)
tort.goto(0,25)
tort.goto(-10,20)
tort.goto(0,25)
tort.goto(10,20)
tort.goto(0,25)
tort.goto(0,30)
tort.left(90)
tort.circle(10,360) 
tort.penup()
tort.goto(-4,42)
tort.pendown()
tort.goto(-3,42)
tort.penup()
tort.goto(4,42)
tort.pendown()
tort.goto(3,42)
tort.penup()
tort.goto(0,35)
tort.pendown()
tort.circle(5,30)
tort.penup()
tort.goto(0,35)
tort.pendown()
tort.circle(5,-30)
tort.penup()
tort.goto(1000,1000)

wn = turtle.Screen()
wn.mainloop()
