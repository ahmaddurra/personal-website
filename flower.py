import turtle
turtle.shape("turtle")
radius=50

def draw_circle(color):
	turtle.fillcolor(color)
	turtle.begin_fill()
	turtle.circle(radius)
	turtle.end_fill()
	turtle.left(60)

def draw_flower():
	draw_circle("red")
	draw_circle("orange")
	draw_circle("yellow")
	draw_circle("green")
	draw_circle("blue")
	draw_circle("purple")
for x in range (6):
	draw_flower()
	turtle.left(60)
	turtle.up()
	turtle.fd(100)
	turtle.down()


turtle.exitonclick()
