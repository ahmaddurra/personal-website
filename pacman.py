from turtle import *
import turtle
SCREEN_WIDTH=400
SCREEN_HEIGHT=400
turtle.screensize(SCREEN_WIDTH,SCREEN_HEIGHT)
turtle.setup(SCREEN_WIDTH,SCREEN_HEIGHT)
class Ball(Turtle):
	def __init__(self,x,y,dx,dy,r,Color):
		Turtle.__init__(self)
		self.penup()
		self.x = x
		self.y = y
		self.goto(self.x,self.y)
		self.dx=dx
		self.dy=dy
		self.r=r
		self.shape("circle")
		self.shapesize(r/10)
		self.color(Color)
pacman_x=10
pacman_y=10	
pacman_r=10
pacman_dx=10
pacman_dy=10
pacman_color="yellow"
pacman= Ball(pacman_x,pacman_y,pacman_dx, pacman_dy, pacman_r, pacman_color)	
def up():
	while True:
		current_y=pacman.ycor()
		current_x=pacman.xcor()
		new_y=current_y+pacman_dy
		new_x=current_x
		pacman.goto(new_x,new_y)
		if turtle.onkey("Down"):
def down():
	while True:
		current_y=pacman.ycor()
		current_x=pacman.xcor()
		new_y=current_y-pacman_dy
		new_x=current_x
		pacman.goto(new_x,new_y)
def right():
	while True:
		current_y=pacman.ycor()
		current_x=pacman.xcor()
		new_y=current_y
		new_x=current_x+pacman_dx
		pacman.goto(new_x,new_y)
def left():
	while True:
		current_y=pacman.ycor()
		current_x=pacman.xcor()
		new_y=current_y
		new_x=current_x
		pacman.goto(new_x,new_y)
def move_on_click():
	turtle.onkey(up, "Up")
	turtle.onkey(down, "Down")
	turtle.onkey(right,"Right")
	turtle.onkey(left,"Left")
	turtle.listen()


while True: 
	
	move_on_click()
	turtle.exitonclick()