from turtle import Turtle
import turtle
import random
from turtle import *
colormode(255)
class Square(Turtle):
	def __init__(self,size):
			Turtle.__init__(self)
			self.shapesize(size)
			self.shape("square")
			
	def random_color(self):
		R=random.randint(0,255)
		G=random.randint(0,255)
		B=random.randint(0,255)
		color=(R,G,B)
		self.color(color)

#square1=Square(10)
#square1.random_color()
class Hexagon(Turtle):
	def __init__(self,size,color,speed):
		Turtle.__init__(self)
		self.shapesize(size)
		turtle.begin_poly()
		for x in range(6):
			turtle.rt(60)
			turtle.fd(10)
		turtle.end_poly()
		h=turtle.get_poly()
		register_shape("hexagon", h)
		self.shape("hexagon")
		self.color(color)
		self.speed(speed)


#hexagon1=Hexagon(5,"red",1)
class Polygon(Turtle):
	def __init__(self,size,lines):
		Turtle.__init__(self)
		
		self.shapesize(size)
		turtle.begin_poly()
		for x in range(lines):
			turtle.rt(360/lines)
			turtle.fd(1)
		turtle.end_poly()
		p=turtle.get_poly()
		register_shape("polygon",p)
		self.shape("polygon")

polygon1=Polygon(3,189)


polygon1.fd(100)

mainloop()




