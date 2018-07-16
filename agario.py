import turtle
import time
import random 
from ball import Ball
import math
from Tkinter import *
#question,option#1,#2,#3,#4,right answer
questions=[['1+1',1,3,4,2,2],['2*2',2,4,6,5,4],['2*3',4,6,3,9,6],['2*4', 6,9,4,8,8],['5*6',20,30,24,24,30],['9*8',90,56,49,72,72],['75/15',15,5,3,4,5],['51/3',15,18,14,17,17],['13*3',29,26,39,37,39],['12*4',46,40,84,48,48]]
ABC=['A','B','C','D']
master = Tk()
turtle.tracer(0)
turtle.colormode(255)
turtle.hideturtle()
RUNNING= True
SLEEP=0.0077
SCREEN_WIDTH=((turtle.getcanvas().winfo_width()/2)+200)
SCREEN_HEIGHT=((turtle.getcanvas().winfo_height()/2)+200)

NUMBER_OF_BALLS=10
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 70
MINIMUM_BALL_DX = -1
MAXIMUM_BALL_DX = 1
MINIMUM_BALL_DY = -1
MAXIMUM_BALL_DY = 1
my_ball_x=20
my_ball_y=20
my_ball_dx=1
my_ball_dy=1
my_ball_r=50

my_ball_color="red"
MY_BALL=Ball(my_ball_x,my_ball_y,my_ball_dx,my_ball_dy,my_ball_r,my_ball_color)

BALLS=[]

my_ball_x= 20
my_ball_y= 20
my_ball_dx =1
my_ball_dy =1
my_ball_r = 40
my_ball_color ="red"
# MY_BALL = Ball(my_ball_x,my_ball_y,my_ball_dx,my_ball_dy,my_ball_r,my_ball_color)
BALLS=[]
for i in range (NUMBER_OF_BALLS):
	x=random.randint(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS, SCREEN_WIDTH-MAXIMUM_BALL_RADIUS)
	while x==my_ball_x:
		x=random.randint(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS, SCREEN_WIDTH-MAXIMUM_BALL_RADIUS)
	y=random.randint(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS)
	while y==my_ball_y:
		y=random.randint(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS)
	dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
	while dx==0:
		dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)

	dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
	while dy==0:
		dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
	r=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
	R=random.randint(25,255)
	G=random.randint(0,255)
	B=random.randint(0,255)	
	color=(R,G,B)
	balli=Ball(x,y,dx,dy,r,color)
	balli.shapesize(r/10)
	BALLS.append(balli)

def move_all_balls():
	for h in BALLS:
		h.move(SCREEN_WIDTH,SCREEN_HEIGHT)
def collide(ball_a,ball_b):
	if ball_a==ball_b:
		return False
	d=math.sqrt(math.pow((ball_a.xcor()-ball_b.xcor()),2)+math.pow((ball_a.ycor()-ball_b.ycor()),2))
	if (ball_a.r+ball_b.r)>=(d+10):
		return True
	else:
		return False

def check_all_balls_collision():
	for ball_a in BALLS:
		for ball_b in BALLS:
			if (collide(ball_a,ball_b)):
				ball_a_r=ball_a.r 
				ball_b_r=ball_b.r
				new_r=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
				new_x=random.randint(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS, SCREEN_WIDTH-MAXIMUM_BALL_RADIUS)
				new_y=random.randint(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS)
				while (my_ball_x+my_ball_r>=new_x- new_r) and (my_ball_x-my_ball_r<=new_x+ new_r)and (my_ball_y-my_ball_r<=new_y+ new_r)and (my_ball_y+my_ball_r>=new_y- new_r):
					new_x=random.randint(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS, SCREEN_WIDTH-MAXIMUM_BALL_RADIUS)
					new_y=random.randint(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS)
				
				new_dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
				while new_dx==0:
					new_dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)

				new_dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
				while new_dy==0:
					new_dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
			
				R=random.randint(0,255)
				G=random.randint(0,255)
				B=random.randint(0,255)	
				new_color=(R,G,B) 
				if ball_a_r>ball_b_r:
					ball_b.goto(new_x,new_y)
					ball_b.dx=new_dx
					ball_b.dy=new_dy
					ball_b.r=new_r
					ball_b.color=new_color
					ball_b.shapesize(new_r/10)
					ball_a.r=ball_a_r+2
					ball_a.shapesize(ball_a.r/10)
				elif ball_b_r>ball_a_r:
					ball_a.goto(new_x,new_y)
					ball_a.dx=new_dx
					ball_a.dy=new_dy
					ball_a.r=new_r
					ball_a.color=new_color
					ball_a.shapesize(new_r/10)
					ball_b.r=ball_b_r+2
					ball_b.shapesize(ball_b.r/10)
def check_myball_collision():
	for ball in BALLS:
		if(collide(MY_BALL,ball)):
			new_r2=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
			new_x2=random.randint(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS, SCREEN_WIDTH-MAXIMUM_BALL_RADIUS)
			new_y2=random.randint(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS)
			while (my_ball_y-MY_BALL.r<=new_y2+new_r2)and (my_ball_y+MY_BALL.r>=new_y2-new_r2) and (my_ball_x-MY_BALL.r<=new_x2+new_r2) and (my_ball_x+MY_BALL.r>=new_x2-new_r2):
				new_x2=random.randint(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS, SCREEN_WIDTH-MAXIMUM_BALL_RADIUS)
				new_y2=random.randint(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS)
			new_dx2=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
			while new_dx2==0:
				new_dx2=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)

			new_dy2=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
			while new_dy2==0:
				new_dy2=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
		
			R=random.randint(0,255)
			G=random.randint(0,255)
			B=random.randint(0,255)	
			new_color2=(R,G,B) 
			
			ball_r=ball.r
			if MY_BALL.r<ball_r:
				print 'collide'
				return True

			
			 
			else: 

				ball.goto(new_x2,new_y2)
				ball.dx=new_dx2
				ball.dy=new_dy2
				ball.r=new_r2
				ball.color=new_color2
				my_ball_r=MY_BALL.r
				MY_BALL.r= my_ball_r+3
				ball.shapesize(new_r2/10)
				
				MY_BALL.shapesize(MY_BALL.r/10)
				

			
	return False
def right():
	p_x=random.randint(-(SCREEN_WIDTH-200)+MAXIMUM_BALL_RADIUS, (SCREEN_WIDTH-200)-MAXIMUM_BALL_RADIUS)
	p_y=random.randint(-(SCREEN_HEIGHT-200)+MAXIMUM_BALL_RADIUS,(SCREEN_HEIGHT-200)-MAXIMUM_BALL_RADIUS)
	MY_BALL.goto(p_x,p_y)
	print 'right'
	master.quit()
def wrong():
	RUNNING=False
	master.quit()
	turtle.bye()
def askQ():
	Q=random.randint(0,len(questions)-1)

	Button(master, text='A', command=wrong).grid(row=3, column=0, sticky=None, pady=4)
	Button(master, text='B', command=wrong).grid(row=3, column=1, sticky=None, pady=4)
	Button(master, text='C', command=wrong).grid(row=4, column=0, sticky=None, pady=4)
	Button(master, text='D', command=wrong).grid(row=4, column=1, sticky=None, pady=4)
	for i in questions[Q][1:-1]:
		if i==questions[Q][-1]:
			Button(master, text=ABC[questions[Q].index(i)-1], command=right).grid(row=(questions[Q].index(i))/2+2, column=(questions[Q].index(i)-1)%2, sticky=None, pady=4)
	row=(int(math.ceil(float(questions[Q].index(i)/2.0))+2))
	Label(master, text=questions[Q][0]).grid(row=0)
	for i in range(len(questions[Q])-2):
		Label(master,text=ABC[i]+':'+str(questions[Q][i+1])).grid(row=i/2+1,column=i%2)

canvas= turtle.getcanvas()
mousex,mousey=canvas.winfo_pointerx(), canvas.winfo_pointery()
def movearound():
	MY_BALL.ondrag(MY_BALL.setpos)
	#MY_BALL.x=MY_BALL.pos()[0]
	#MY_BALL.x=MY_BALL.pos()[1]


#def increase_difficulty():
	
	#if MY_BALL.r>MAXIMUM_BALL_RADIUS:
		#MAXIMUM_BALL_RADIUS=MAXIMUM_BALL_RADIUS+30
		#MINIMUM_BALL_RADIUS=MINIMUM_BALL_RADIUS+20


while RUNNING:
	movearound()
	print MY_BALL.r
	print MY_BALL.shapesize()
	move_all_balls()
	time.sleep(SLEEP)
	turtle.getscreen().update()
	check_all_balls_collision()
	check_myball_collision()
	#increase_difficulty()
	#RUNNING = check_myball_collision()
	
	if check_myball_collision():
		askQ()
		master.mainloop()
	if SCREEN_WIDTH!=((turtle.getcanvas().winfo_width()/2)+200):
		SCREEN_WIDTH=((turtle.getcanvas().winfo_width()/2)+200)
		SCREEN_HEIGHT=((turtle.getcanvas().winfo_height()/2)+200)
	if SCREEN_HEIGHT!=((turtle.getcanvas().winfo_height()/2)+200):
		SCREEN_WIDTH=((turtle.getcanvas().winfo_width()/2)+200)
		SCREEN_HEIGHT=((turtle.getcanvas().winfo_height()/2)+200)

