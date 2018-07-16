fruits = ["apples", "banana", "melon", "grape"]
for x in range (len(fruits)-1,-1,-1):
	word = fruits[x]
	if "a" in word:
		del fruits [x]

print(fruits)
