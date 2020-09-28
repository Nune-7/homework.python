# second version
# from random import randint
# a =["rock", "paper", "scissors?\n"]
# comp = a[randint(0,2)]
# player = False
# s = 0 
# while player == False:
# 	player = input("rock, paper, scissors?\n")
# 	if player == comp:
# 		print("equal score", "your score is", s+1)
# 	elif player == "rock":
# 		if comp == "paper":
# 			print("you loose", comp, "beat", player, "your score is", s)
# 		else:
# 			print("You win", player, "beat", comp, "your score is", s+1)
# 	elif player == "paper":
# 		if comp == "scissors":
# 			print("you loose", comp, "beat", player, "your score is", s)
# 		else:
# 			print("You win", player, "beat", comp, "your score is", s+1)
# 	elif player == "scissors":
# 		if comp == "rock":
# 			print("you loose", comp, "beat", player, "your score is", s)
# 		else:
# 			print("You win", player, "beat", comp, "your score is", s+1)
# 	else:
# 		print("Thats is wrong play. Try again")
# 	player = False
# 	comp = a[randint(0,2)]
# second version
from random import randint
check = "yes"
score_user = 0
score_computer = 0
round_ = 0
while check == "yes":
	user_choice = int(input("tell me 1 for scissors, 2 for paper, 3 for rock"))
	computer_choice = randint(1,3)
	if (user_choice == 1 and computer_choice == 2) or (user_choice == 2 and computer_choice == 3) or (user_choice == 3 and computer_choice == 1):
		score_user +=1
	elif user_choice == computer_choice:
		print("Tie")
	else:
		score_computer +=1
	round_+=1
	check = ""
	while check != "no" and check != "yes":
		check = input("Do you want to play again? yes for yes, no for no")
print(f"Hope you enjoyed\n your score is {score_user}\n, computer score is {score_computer}\n, you have playes {round_} times")