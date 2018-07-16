import turtle
turtle.shape("turtle")
for x in range(5):
	for y in range (5):
		for n in range (4):
			turtle.forward(100)
			turtle.right(90)
		turtle.left(90)
	turtle.forward(100)
turtle.exitonclick()