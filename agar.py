from ball import Ball

import turtle

import time

import random

import math

import numpy as np


from Tkinter import *

master = Tk()

questions = [['1+1',2,5,6,1]]

#face_cascade = cv2.CascadeClassifier('/usr//local//lib//python2.7//dist-packages//cv2//data//haarcascade_frontalface_default.xml')

#eye_cascade = cv2.CascadeClassifier('/usr//local//lib//python2.7//dist-packages//cv2//data//haarcascade_eye.xml')

#cap = cv2.VideoCapture(0)

turtle.colormode(255)

turtle.tracer(0)

turtle.ht()

Running=True

Sleep=0.0077

SCREEN_WIDTH=turtle.getcanvas().winfo_width()/2

SCREEN_HIGHT=turtle.getcanvas().winfo_height()/2

Pause = False

numBalls =1

minR=70

maxR=100

minDX=-5

maxDX=5

minDY=-5

maxDY=5

ABC=['A','B','C','D']

Balls = []

for i in range(numBalls):

	x = random.randint(-SCREEN_WIDTH+maxR,SCREEN_WIDTH-maxR)

	y = random.randint(-SCREEN_HIGHT+maxR,SCREEN_HIGHT-maxR)

	dx = random.randint(minDX,maxDX)

	dy = random.randint(minDY,maxDY)

	R = random.randint(0,255)

	G = random.randint(0,255)

	B = random.randint(0,255)

	Color = (R,G,B)

	raduius = random.randint(minR,maxR)

	enemyBall = Ball(x,y,dx,dy,raduius,Color)

	Balls.insert(-1,enemyBall)

myBall = Ball(0,0,5,5,50,Color)

def moveAllBalls():

	for i in Balls:

		i.move(SCREEN_WIDTH,SCREEN_HIGHT)

def checkCollision(ballA,ballB):

	if ballA == ballB:

		return False

	elif (math.sqrt((ballA.x-ballB.x)**2+(ballA.y-ballB.y)**2))<ballA.r +ballB.r:

		return True

	return False



def allCollision():

	for Ball1 in Balls:

		for Ball2 in Balls:

			if checkCollision(Ball1,Ball2)==True:

				if Ball1.r >= Ball2.r:

					pass

					#Ball1.r = Ball1.r +0.001

					#Ball1.shapesize(Ball2.r/10)

					#Ball2.dx = -Ball2.dx

					#Ball2.dy = -Ball2.dy

					#Ball2.y = random.randint(-SCREEN_WIDTH+maxR,SCREEN_WIDTH-maxR)

					#Ball2.y = random.randint(-SCREEN_HIGHT+maxR,SCREEN_HIGHT-maxR)

				else:

					pass

					#Ball2.r = Ball2.r +0.001

					#Ball2.shapesize(Ball2.r/10)

					#Ball1.dx = -Ball1.dx

					#Ball1.dy = -Ball1.dy



def myBallcollision():

	for ball in Balls:

		if checkCollision(myBall,ball):

			if myBall.r>ball.r:

				Balls.remove(ball)

				ball.hideturtle()

				myBall.r = myBall.r +1

				myBall.shapesize(myBall.r/10)

			elif myBall.r<ball.r:

				return True

canvas = turtle.getcanvas()

mousex, mousey = canvas.winfo_pointerx(), canvas.winfo_pointery()

def followMouse():

	myBall.ondrag(myBall.setpos)

	myBall.x = myBall.pos()[0]

	myBall.y = myBall.pos()[1]



while True:

	if myBallcollision():

		askQ()

		mainloop()

	moveAllBalls()

	allCollision()

	turtle.getscreen().update()

	time.sleep(Sleep)

	followMouse()