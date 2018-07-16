import turtle
turtle.shape("turtle")

for x in range(10):
	turtle.right(36)
	for x in range(4):
		turtle.forward(100)
		turtle.right(90)

turtle.exitonclick()

