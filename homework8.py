# ex.1
from functions import area_t
n = area_t(4,6)
print(n)
# ex.2
a = input("tell me a word\n")
from functions import str_
word = str_(a)
print(word)
 # ex.3
a = input("tell me something\n")
c1 = 0
c2 = 0
for i in a:
	if (i.isupper()) == True:
		c1 += 1
	elif (i.islower()) == True:
		c2 += 1
print("the number of uppercases in that string are`", c1)
print("the number of lowercases in that string are`", c2)
# ex.4
a = input("tell me something\n")
def str_(a):
	rev_str = a[::-1]
	return rev_str
word = str_(a)
print(word)
if word in a:
	print(a,"is a palindrome string\n")
else:
	print(a,"is not polindrome string\n",a)


