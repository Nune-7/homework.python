# ex.1
 a = int(input("tell me a number\n"))
 for i in range(a-1,12):
 	print("{}+{}={}".format(i+1,i,2*i+1))
# ex.2
 a = input("what you think about the weather? is it cold?\n")
  # print(a)
 s = 0
 for i in a:
 	if i.isdigit():
 		s+=1
 print(s)
 # ex.3
 for i in range (1,11):
 	print(i*str(i))
a = input("give me a row from 1 to 9\n")
for i in a:
	print(i*int(i))