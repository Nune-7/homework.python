# number = input("tell mme a numebr and I'll return the half of it\n")
# try:	
# 	half = int(number)/2
# except ValueError:
# 	print("Value is not difine")
# num_1 = int(input("tell me a number to divide 4 with\n"))
# try:
# 	new_value = 4 / num_1
# except ZeroDivisionError:
# 	print("It is ZeroDivisionError")
# try:
# 	print(hello)
# except NameError:
# 	print("It is Nameerror")



# input_ = input("Tell me a number\n")
# try:
# 	input_ = int(input_)
# except ValueError:
# 	input_ = input("tell me a number")
# 	try:
# 		input_ = int(input_)
# 	except:
# 		print("ok")
# 		input_1 = 1
# summery_ = input_ + 5

check = True
while check:
	try:
		password = input("Tell me a password\n")
		if len(password) < 8:
			raise ValueError(" It should be at least 8 ")
		check_number = False
		for i in password:
			if i.isdigit():
				check_number = True
			if not i.isalpha():
				if i !=" ":
					break
				else:
					raise NameError("The password could nor contain a space")
		if not check_number:
			raise TypeError("Should contain a number")
		if password[0].islower():
			raise Exception("Should start with a capital letter")
		check = False
	except TypeError as t:
		print(t)
	except ValueError as v:
		print(v)
	except NameError as e:
		print(n)
	except Exception as exc:
		print(exc)
print(F"{password}" "is strong one thanks!!!")


