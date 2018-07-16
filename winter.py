from turtle import *
import random
import math
class Ball (Turtle):
	def __init__(self, radius,color, speed):
		turtle.__init__(self)
		self.shape("cricle")
		self.shapesize(radius/10)
		self.radius=radius
		self.color(color)
		self.speed(speed)
def check_collision(ball1,ball2):
	d=math.sqrt(math.pow((ball1.x-ball2.x),2)+math.pow((ball1.y-ball2.y),2))
	if (ball1.radius+ball2.radius)>=d:
		return True
	if True:
		ball1.color="green"
		ball2.color="blue"




def top(self):
	returnself.ycor()+self.h/2