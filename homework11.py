# ex.1
dict1={1:10, 2:20}
dict2={3:30, 4:40}
dict3={5:50,6:60}
dict4={6:50,7:60}
dict5 = {}
# firstversion
a = dict1.update(dict2)
b = dict1.update(dict3)
c = dict1.update(dict4)
print(dict1)
# second version
for i in dict1:
	if i in dict1:
		dict5[i] = dict1[i]
for j in dict2:
	if j in dict2:
		dict5[j] = dict2[j]
for k in dict3:
	if k in dict3:
		dict5[k] = dict3[k]
for l in dict4:
	if l in dict4:
		dict5[l] = dict4[l]
print(dict5)

# ex.2

dict1 = {1:1,2:2,3:3,4:4,5:5}
dict2 = {}
for i in dict1:
	dict2[i]= dict1[i]*dict1[i]
print(dict2)

# ex.3
a = {"c1":"Red", "c2":"Grean", "c3":"None"}
del a["c3"]
print(a)









