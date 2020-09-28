a = input("Hi,\nwe pleased you prefer to be our guest tonight and to taste our dishes.what about dishes we have\npizza=500\nqebab=550")
c = input(a)
print(c)
b = input("and what about adds? \nketchup=200\nmayonez=300")
d = input(b)
print(d)
e = int(c) + int(d)
print("you have ordered pizza and ketchup and your price is 700", e==700)
print("you have ordered pizza and mayonez and your price is 800", e==800)
print("you have ordered qebab and ketchup and your price is 600", e==600)
print("you have ordered qebab and mayonez and your price is 850", e==850)
# ex.2
a = input("tell me the day number\n")
num =int(a)
if num == 0:
	print("sunday")
elif num == 1:
    print("monday")
elif num == 2:
    print("tuesday")
elif num == 3:
    print("wednesday")
elif num == 4:
    print("thursday")
elif num == 5:
    print("friday")
elif num == 6:
    print("saturday")
# ex.3
a=input("is it raining?\n")
if " " in a:
	print("it is a centenses")
else:
	print("it is a word")
ex.4
a = input("what do you think about this movie?")
b = len(a)
c = "ing"
d = "ly"
print(a)
print(len(a))
if b > 3:
	print(a+c)
if b < 3:
	print(a)
if c in a:
	print(a+d)

 


