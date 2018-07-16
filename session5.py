class animal(object):
	def __init__(self, name,species,age,favorite_color):
		self.name=name
		self.species=species
		self.age=age
		self.favorite_color=favorite_color
class Cat(animal):c
	def meow(self, sound):
		print(sound+" wana mashi,"+ " wana mashi ma3aa")
johnny_mashi=Cat(name="johnny_mashi",species="cat",age="17", favorite_color="blue")
print(johnny_mashi.name)
johnny_mashi.meow("johhny mashi,")
class bird(animal):
	def fly(self, action):
		print(action+" high "+action+" drunk")
russ=bird("russ","bird","2","green")
russ.fly("inbetween")
class chicken(bird):
	def cant_fly(self, zahgan):
		print("sho sawena.. " +zahgan+". bi 3enena.. "+zahgan) 
tamer=chicken("tamer","bird","17","green")
tamer.cant_fly("i7rig george")
class dove(bird):
	def laying_eggs(self, egg):
		print("I am laying "+egg)
hashem=dove("hashem","bird","17","blue")
hashem.laying_eggs("hashoom")
class fish(animal):
	def swim(self):
		print("my dream is to fly")
durra=fish("durra","fish","17","blue")
durra.swim()
import turtle
class ball(Turtle):
	def __init__(self,size,color):
		Turtle.__init__(self)
		self.color(color)
		self.shapesize(size)
		self.shape("circle")
circle1=ball(10,"blue")
turtle.shape("turtle")
turtle.exitonlick()