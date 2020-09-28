# def my_f(a,b):
# 	c = a + b
# 	return c
# d = my_f("Mane", " HBD!")
# print(d)

# def my_f(a):
# 	b = f"HBD dear {a}"
# 	return b
# greating = my_f("Mane")
# print(greating)

# a = input("Tell me your name")
# def my_f(a):
# 	b = f"HBD dear {a}"
# 	return b
# greating = my_f(a)
# print(greating)

# def sum_1(a,b,c=0):
# 	v = a + b + c
# 	print(v)
# sum_1(2,1)
# sum_1(2,1,3)

# v = "Hallo"
# def sum_1(a,b,c=0):
# 	global v
# 	v = a + b + c
# sum_1(2,1,4)
# print(v)
# import random
# from random import randint
# help(randint)
# print(randint.__doc__)
# def my_f(a: str, b: str):
# 	print(my_f.__annotations__)

# n = int(input("Enter the number\n"))
# fact = 1
# if n < 0:
# 	print("factorial doesn't exist for negative numbers\n")
# else:
# 	for n in range(1,n+1):	
# 		fact = fact * n
# print("the factorinal of",n,"is",fact)
# def factorial_func(a):
# 	if a <= 0:
# 		b = 1
# 	else:
# 		b = a* factorial_func(a-1)
# 	return b
# print(factorial_func(5))

# def factorial_func(a):
# 	a_1 = 1
# 	for i in range(1, a+1):
# 		a_1 *=1
# 	return a_1

# def v_1(a,b,c=1):
# 	v = a*b*c
# 	return v
# print(v_1(1,2))

# def volume_(a,b,c):
# 	volume = a*b*c
# 	print(volume_)
# a_input = int(input("tell me the parametres"))
# b_input = int(input("tell me the parametres"))
# c_input = int(input("tell me the parametres"))

# volume_(a_input, b_input, c_input)

# from random import randint
# check = "yes"
# score_user = 0
# score_computer = 0
# round_ = 0
# while check == "yes":
# 	user_choice = int(input("tell me 1 for scissors, 2 for paper, 3 for rock"))
# 	computer_choice = randint(1,3)
# 	if (user_choice == 1 and computer_choice == 2) or (user_choice == 2 and computer_choice == 3) or (user_choice == 3 and computer_choice == 1):
# 		score_user +=1
# 	elif user_choice == computer_choice:
# 		print("Tie")
# 	else:
# 		score_computer +=1
# 	round_+=1
# 	check = ""
# 	while check != "no" and check != "yes":
# 		check = input("Do you want to play again? yes for yes, no for no")
# print(f"Hope you enjoyed\n your score is {score_user}\n, computer score is {score_computer}\n, you have playes {round_} times")













