
def is_prime(number):
	for x in range (2, number):
		if(number%x==0):
			return False
	return  True

p = is_prime(7)	
print(p)		