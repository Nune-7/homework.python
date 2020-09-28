# for i in range(1,11):
# 	for j in range(1,11):
# 		print(f"This is for\n {i}*{j}={i*j}")
# for i in range(1,9,2):
# 	print(i)
# 	for j in range(0,10,2):
#  		print(f"{i}*{j}={i*j}")
# for i in range(1,12):
# 	print(i* str(i))
# 	if i == 6:
# 		for j in range(5,0,-1):
# 			print(j* str(j))
# 		break
# 	else:
# 		for j in range(5,0,-1):
# 			print(j* str(j))	
# 2nd version
for i in range(1,7):
	print(i* str(i))
	if i == 6:
		for j in range(5,0,-1):
			print(j* str(j))

# a = input("tell me a password\n")
# while len(a) < 8:
# 	a = input("tell me a password\n")

# print("right passwod", a)


# a = input("tell me a password\n")
# while len(a) < 8 and "." in a:
# 		a = input("tell me a password\n")

# print("right passwod", a)
# a = True
# while a:
# 	p = input("tell me a password\n")
# 	if len(p)>8:
# 		if "." in p:
# 			a = False
# print("it is good one")
# import random
# b = random.randint(4,6)
# print(b)
# a = input("tell me a number\n")
# while int(a) != b:
# 	a = input("tell me a password\n")

# print("Right!")
# import random
# b = random.randint(1,5)
# c = 0
# print(b)
# a = input("tell me a number\n")
# while int(a) != b:	
# 	a = input("this is false, tell me a password\n")
# while int(a) == b:
# 	print()
import random
i = 0
user_score = 0 
while i < 5:
	user_answer = int(input("tell me a number\n"))
	random_number = random.randint(1,5)
	if user_answer == random_number:
		user_score += 1
	i += 1
print(f"your score is {user_score}")


user_check = "y"
user_score = 0 
while user_check == "y":
	user_answer = int(input("tell me a number\n"))
	random_number = random.randint(1,5)
	if user_answer == random_number:
		user_score += 1
	user_check = input("Do you want to play: y for  yes !")
	rounds += 1
print(f"your score is {user_score}, you have played {rounds} time")



