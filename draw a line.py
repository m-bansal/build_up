import turtle
t = turtle.Turtle()
t.hideturtle()

t.pensize(5)#for thickness

x=int(input("Enter the number of pixels by which a turtle should be moved: "))

t.forward(x)#distance moved by turtle

turtle.done()
