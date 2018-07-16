from turtle import *

class Ball(Turtle):
	def __init__(self,x,y,dx,dy,r,Color):
		Turtle.__init__(self)
		self.penup()
		self.x=x
		self.y =y
		self.goto(x,y)
		self.dx=dx
		self.dy=dy
		self.r=r
		self.shape("circle")
		self.shapesize(r/10)
		self.color(Color)
	def move(self,screen_width,screen_height):
		current_x=self.xcor()
		new_x= current_x + self.dx
		current_y=self.ycor()
		new_y=current_y+self.dy
		right_side_ball=new_x+self.r
		left_side_ball=new_x-self.r
		top_side_ball=new_y+self.r
		bottom_side_ball=new_y-self.r
		if right_side_ball>screen_width:
			self.dx= -self.dx
		elif left_side_ball<-screen_width:
			self.dx= -self.dx
		if top_side_ball>screen_height:
			self.dy= -self.dy
		elif bottom_side_ball<-screen_height:
			self.dy= -self.dy
		self.goto(new_x,new_y)

                                                                                                                 