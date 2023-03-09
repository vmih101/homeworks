import turtle

turtle.title("Turtle Drawing")

spiral = turtle.Turtle()
spiral.pensize(2)
spiral.speed(10)

x = 5
while x < 205:
    spiral.forward(x)
    spiral.right(90)
    x += 5

star = turtle.Turtle()
star.penup()
star.goto(-200,-200)
star.pendown()
star.shape("turtle")

for i in range(12):
    star.fd(100)
    star.stamp()
    star.bk(100)
    star.rt(30)
star.ht


circles = turtle.Turtle()
circles.penup()
circles.goto(200,200)
circles.pendown()
circles.speed(10)
circles.left(60)

for i in range(5):
    circles.circle(-75)
    circles.right(60)
circles.circle(-75, 180)

turtle.exitonclick()