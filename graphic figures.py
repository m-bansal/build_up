import turtle
t = turtle.Turtle()

t.pensize(4)#for thickness
t.hideturtle()

#line
line=int(input("Enter the number of pixels by which a turtle should be moved to draw a line: "))
t.forward(line)#distance moved by turtle

t.penup()#move the turtle head
t.goto(0, -200)#no outline drawn by turtle
t.pendown()#start outlining


#square
x=int(input("Enter the number of pixels by which a turtle should be moved for square: "))
for i in range(4):
    t.forward(x)#distance moved by turtle
    t.left(90)


t.penup()#move the turtle head
t.goto(0, -x)#no outline drawn by turtle
t.pendown()#start outlining


#rectangle
l=int(input("Enter the length for rectangle: "))
b=int(input("Enter the breadth for rectangle: "))
for i in range(2):
    t.forward(l)
    t.left(90)
    t.forward(b)
    t.left(90)

turtle.done()
