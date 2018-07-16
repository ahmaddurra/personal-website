import turtle
turtle.shape("turtle")
class Ball(Turtle):
	def __init__(self,x,y,dx,dy,r,color):
		turtle.__init__(self)
		turtle.penup()
		self.x=x
		self.y=y
		self.dx=dx
		self.dy=dy
		self.r=r
		self.shape("circle")
		self.shapesize=r/10
		self.color("color")
	def move(self,screen_width,screen_height):
		current_x=self.x
		new_x=current_x+self.dx
		current_y=self.y
		new_y=current_y+self.dy
		right_side_ball=new_x+r
		left_side_ball=new_x-r
		top_side_ball=new_y-r
		bottom_side_ball=new_y+r
turtle.goto(0,0)
