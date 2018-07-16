import turtle
turtle.shape("turtle")
length=425
width=575
hypotenuse=300
third_length=141.6
inner_side=435
turtle.up()

turtle.back(200)
turtle.left(90)
turtle.back(100)

turtle.down()
turtle.fillcolor("red")
turtle.begin_fill()
turtle.fd(length)
turtle.right(135)
turtle.fd(hypotenuse)
turtle.right(90)
turtle.fd(hypotenuse)
turtle.end_fill()

turtle.fillcolor("green")
turtle.begin_fill()
turtle.left(135)
turtle.fd(width)
turtle.left(90)
turtle.fd(third_length)
turtle.left(90)
turtle.fd(inner_side)
turtle.end_fill()

turtle.rt(135)
turtle.fd(100)
turtle.lt(90)
turtle.fd(100)
turtle.rt(135)

turtle.fillcolor("black")
turtle.begin_fill()
turtle.fd(inner_side)
turtle.lt(90)
turtle.fd(third_length)
turtle.lt(90)
turtle.fd(width)
turtle.end_fill()

turtle.exitonclick()