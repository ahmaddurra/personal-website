print(4+3)
print(4-3)
print(4/3)
print(4*3)
print(4.0/3.0)
print(4.5/3)
print(21%2)
print(14%17)
print(15%3)
print(14.5%8)

for x in range (7):
	print(x%2)
print(5==5)
print(5==4)
print(5%4==1)

for x in range (8):
	if((x%2)==0):
		print(x)

import turtle
turtle.shape("turtle")
for y in range(7):
	if(x%2==0):
		#draw high line
		turtle.fd(100)
		turtle.rt(90)
		turtle.up()
		turtle.fd(50)
		turtle.down()
		turtle.lt(50)
	# if(x%2==1):
	#draw line and space
# turtle.fd(100)
# turtle.up()
# turtle.fd(50)
# turtle.down()
turtle.exitonclick()