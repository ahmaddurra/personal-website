import turtle
turtle.shape("turtle")
input=1
length=100
ra=90
#draw square
if(input==1):
	turtle.fillcolor("red")
	turtle.begin_fill()
	for x in range(4):
		turtle.forward(length)
		turtle.rt(ra)
	turtle.end_fill()	

#draw circle
elif(input==2):
	turtle.fillcolor("green")
	turtle.begin_fill()
	turtle.circle(50)
	turtle.end_fill()
#draw rectangle
elif(input==3):
	turtle.fillcolor("orange")
	turtle.begin_fill()
	for y in range (2):
		turtle.fd(length)
		turtle.rt(ra)
		turtle.fd(50)
		turtle.rt(ra)
	turtle.end_fill()

#draw triangle
elif(input==4):
	turtle.fillcolor("black")
	turtle.begin_fill()
	for n in range(3):
		turtle.fd(length)
		turtle.lt(120)
	turtle.end_fill()	


turtle.exitonclick()