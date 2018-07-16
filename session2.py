list2=["can","we","mix","values","types","with",5,7,"and",True,False]
import turtle
turtle.shape("turtle")
for y in range(3):
	turtle.up()
	turtle.fd(60)
	turtle.down()

	for x in range(4):
			for i in range(4):
				turtle.fd(30)
				turtle.rt(90)
			turtle.fd(30)
			turtle.lt(90)
turtle.fd(60)
turtle.rt(90)
turtle.fd(30)
turtle.rt(90)
turtle.fd(210)
turtle.rt(90)
turtle.fd(90)
turtle.rt(90)
turtle.fd(210)
turtle.rt(90)
turtle.fd(30)



turtle.exitonclick()