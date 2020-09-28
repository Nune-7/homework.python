# a = input("Tell me how many days in this year\n")
# if a.endswith("5"):
#     print("it's not a leap year\n")
# elif a.endswith("6"):
#     print("it's a leap year")
# second version
# a = input("Tell me the year?\n")
# b = int(a) % 4
# if b ==0:
# 	print("it's a leap year")
# elif b != 0:
# 	print("it's not")
# ex. 2
# a = input("Tell me a number\n")
# b = int(a) % 5
# c = int(a) % 11
# # print(b)
# # print(c)
# if b == 0 or c == 0:
#     print("it's division 5 or 11")
# elif b != 0 or c != 0:
# 	print("it's not division 5 or 11")
# ex. 3
# a = input("give me a number\n")
# b = int(a) % 3
# c = int(a) % 5
# txt1 = "{b} is {d}".format(b = "this", d = "Fizz")
# txt2 = "{c} is {e}".format(c = "this", e = "Buzz")
# txt3 = "{f} is {g}".format(f = "this", g = "FizzBuzz")
# txt4 = "{} is {}".format("This", int(a))
# if b==0 and c!=0:
#     print(txt1)
# elif c==0 and b!=0:
#     print(txt2)
# elif b==0 and c==0:
#     print(txt3)
# else:
#     print(txt4)
# ex. 4
# a = input("I would like to hear what you think about movie we've seen lately. I liked it...\nDid you like it?\t\n")
# b = "good"
# k = a.strip("poor")
# # print(k)
# d =k.replace("not", b)
# # print(d)
# len1=d[:d.find(b)+5]
# print(len1)
# if "not" in a:
# 	print(len1)
# else:
# 	print(a)
# ex.5
# a = input("tell me a letter that is used in this sentence\n")
# b = "restart"
# d = b.find("r")
# e = b[:-6]
# # print(e)
# g = b.replace("r", "$")
# if e == "r":
#  	print(str(b[:-6])+str(b.replace("r", "$")))

