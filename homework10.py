# ex.1
list1 = [[10,20],[40],[30,56,25,25],[10,20],[33],[40]]
list1 = dict.fromkeys(list1)
print(list1)
# i = list1.pop()
# print(i)
# for i in list1:
# 	if i == list1:
# 		# i += b
# 		i = list1.remove(i)
# 	else:
# 		continue
# print(list1)
# ex.2
# list1 = [0,10,[20,30],40,50,[60,70,80],[90,100,110,120]]
# print(list1[2])
# print(list1[5])
# print(list1[6])
# list2 = [0,10, list1[2]]
# ex.3
list1 = [1,1,2,3,4,4,5,1]
print(list1[3:8])
print(list1[0:3])
list2 = list1[3:8], list1[0:3]
print(list2)
# # ex.4
for i in range(1,5):
	if i < 5:
		try:
			a = int(input("tell me a number\n"))
		except ValueError:
			print("you've given me a text, tell me a number\n")	
	elif i > 5:
		try:
			a = int(input("tell me a number\n"))
		except:
			print("This is a string type")
print(i + 1)

# # ex.5
def str_():
'''
#  --- --- --- 
# |   |   |   | 
#  --- --- ---  
# |   |   |   | 
#  --- --- ---  
# |   |   |   | 
#  --- --- ---

 '''
print(str_.___doc___)





