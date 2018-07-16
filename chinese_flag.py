import turtle
turtle.shape("turtle")

#draw rectangle
turtle.fillcolor("red")
turtle.begin_fill()
for x in range(2):
	turtle.fd(300)
	turtle.lt(90)
	turtle.fd(200)
	turtle.lt(90)
turtle.end_fill()

turtle.up()
turtle.lt(60)
turtle.fd(150)

#drawing the big star
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.lt(60)
for m in range(6):
	turtle.fd(30)
	turtle.lt(110)
turtle.end_fill()	

turtle.exitonclick()