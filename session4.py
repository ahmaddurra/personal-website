import random
import turtle
turtle.speed(0.8)
class animal(object):
	def __init__(self,sound,name,age,favorite_color):
		self.sound = sound
		self.name = name
		self.age = age
		self.favorite_color = favorite_color
	def eat(self, food):
		print("Yummy!!" + self.name + " is eating " + food)
	def description(self):
		print(self.name + " is" + self.age + " years old and loves the color " + self.favorite_color)
	def make_sound(self,num):
		print(self.sound*num)
class person(object):
	def __init__(self, name, age, gender):
		self.age = age
		self.name = name
		self.gender = gender
	def eat(self, food):
		print("Yummy!!" + self.name + " is eating " + food)
	def sleep(self):
		print(self.name + " is sleeping")
words = []
colors = ['yellow', 'red', 'blue', 'purple']
class song(object):	
	def add_lyrics(self, lyrics):
		words.append(lyrics)
	def sing_a_song(self):
		for i in words:
			color = colors[random.randint(0,len(colors)-1)]
			turtle.fillcolor(color)
			turtle.begin_fill()
			turtle.circle(50)
			turtle.end_fill()
			print i
	def sing_random(self):
		for i in range(len(words)):
			num = random.randint(0,len(words)-1)
			print words[num]
			del(words[num])

cat = animal("meow ", "minmin", " 69", "red")
ta7sheesh = person("ta7sheesh", 3, "male")
save_me= song()
save_me.add_lyrics("save me")
save_me.add_lyrics("before i fall")
save_me.sing_a_song()
turtle.exitonclick()