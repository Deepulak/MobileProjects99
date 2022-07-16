import turtle
import random

class analog:
	def __init__(self):
		self.color1 = random.random(), random.random(), random.random()
		self.color2 = random.random(), random.random(), random.random()
		turtle.screensize(canvwidth=600, canvheight=600)
		turtle.speed(10)
		turtle.ht()
		turtle.pensize(2)
		turtle.up()
		turtle.goto(-300, -300)
		# set pen color
		turtle.color("blue")
		turtle.down()
		# draw the square box (600x600)
		for _ in range(4):
			turtle.fd(600)		# dorward turtle by side units
			turtle.lt(90)
		turtle.up()

	def clockhand(self):
		turtle.goto(0, 0)
		turtle.lt(60)
		turtle.down()
		# draw the 12 needles
		for i in range(1, 13):
			turtle.pensize(3)
			# set pen color black
			turtle.color("black")
			turtle.fd(250)
			# mark the number
			turtle.write(i, font=("verdana", 15, "normal"))
			turtle.goto(0, 0)
			turtle.rt(30)
	def arrow(self):
		turtle.rt(90)
		turtle.begin_fill()
		for i in range(3):
			turtle.forward(8)
			turtle.left(120)
			turtle.forward(8)
		turtle.lt(90)
		turtle.end_fill()

if __name__ == "__main__":
	turtle.clearscreen()
	clock = analog()
	hour = 24
	hour = hour * 100
	minute = 1440
	clock.clockhand()
	from time import sleep
	sleep(90)