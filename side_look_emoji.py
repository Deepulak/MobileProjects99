# part 1
import turtle

mypen = turtle.Turtle()
mypen.color("#ffdd00")
mypen.begin_fill()
mypen.circle(100)
mypen.fillcolor("#ffdd00")
mypen.end_fill()
mypen.home()

# part2
mypen.goto(-40, 100)
mypen.color("#555555")
mypen.begin_fill()
mypen.circle(15)
mypen.color("#ffffff")
mypen.end_fill()
mypen.penup()
mypen.goto(-48, 110)
mypen.pendown()
mypen.color('Black')
mypen.begin_fill()
mypen.circle(5)
mypen.end_fill()
mypen.penup()

# part 3
mypen.goto(40, 100)
mypen.pendown()
mypen.color("#555555")
mypen.begin_fill()
mypen.circle(15)
mypen.color("#ffffff")
mypen.end_fill()
mypen.penup()
mypen.goto(32, 110)
mypen.pendown()
mypen.color('Black')
mypen.begin_fill()
mypen.circle(5)
mypen.end_fill()
mypen.penup()

# part 4
mypen.goto(-20, 50)
mypen.pendown()
mypen.pensize(10)
mypen.forward(40)


turtle.done()
