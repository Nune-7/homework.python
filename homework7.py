# ex.1
n = int(input("Enter the number\n"))
fact = 1
if n < 0:
	print("factorial doesn't exist for negative numbers\n")
else:
	for n in range(1,n+1):	
		fact = fact * n
print("the factorinal of",n,"is",fact)
# ex.2
a = input("ask me a question\n")
import random 
l = ["yes","no"]
for a in range(7):
	r = random.randint(0,1)
	print(l[r])
	b = input((l[r], "ask me a question\t\n"))
# ex.3
q = int(input("enter the terms\n"))
f = 0
s = 1
if q < 0:
	print("the requested series is ", f)
else:
	print(f,s, end=" ")
for i in range(2,50):	
	n = f + s
	print(n, end=" ")
	f = s
	s = n
pass
# ex.4
from random import randint
a =["rock", "paper", "scissors?\n"]
comp = a[randint(0,2)]
player = False
s = 0 
while player == False:
	player = input("rock, paper, scissors?\n")
	if player == comp:
		print("equal score", "your score is", s+1)
	elif player == "rock":
		if comp == "paper":
			print("you loose", comp, "beat", player, "your score is", s)
		else:
			print("You win", player, "beat", comp, "your score is", s+1)
	elif player == "paper":
		if comp == "scissors":
			print("you loose", comp, "beat", player, "your score is", s)
		else:
			print("You win", player, "beat", comp, "your score is", s+1)
	elif player == "scissors":
		if comp == "rock":
			print("you loose", comp, "beat", player, "your score is", s)
		else:
			print("You win", player, "beat", comp, "your score is", s+1)
	else:
		print("Thats is wrong play. Try again")
	player = False
	comp = a[randint(0,2)]
# ex. 5 
n = 10
m = n - 1
for row in range(-m, m+1):
	for col in range(-m, m+1):
		if abs(row) + abs(col) <= m:
			c = "*"
		else:
			c = " "
		print(c, end=" ")
	print()