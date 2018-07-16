a= [5, 10, 15, 20, 25]
def vro(list):
	b=[list[0],list[-1]]
	print b

vro(a)
x = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
def shotgun(list):
	vroo=[]
	for y in range (len(x)):
		if(list[y]<5):
			vroo.append(list[y])
	print vroo		
			
shotgun(x)
o = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
def vro2(list1,list2):
	low=[]
	for i in range(len(list1)):
		for p in range(len(list2)):
			if (list1[i]==list2[p]):
				if(list1[i]not in low):
					low.append(list1[i])
	print low
vro2(o,a)
def vro3(number):
	for x in range(2,number):
		if(number%x==0):
			print "not_prime"
	print "prime" 
vro3(7)



