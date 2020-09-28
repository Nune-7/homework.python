# user_answer = input("tell smth ")
# try:
# 	my_n = int(user_answer)
# 	value = 10 / my_n
# except ValueError:
# 	print("wrong value it is not a digit")
# 	my_n = 0
# except ZeroDivisionError:
# 	print("the number could not b 0")
# 	value = 10
# my_n +=5
# try:
# 	print(value)
# except NameError:
# 	print("you didn't give a number thats why you couldn't see the value")

# a_key = "key1"
# my_dict = {a_key:{1:"2","4":3}, (1,2):5}
# a = my_dict[a_key][1]
# print(a)
# b = my_dict[(1,2)]
# c = my_dict.get((1,2))
# print(b)
# print(c)

# a_key = "key1"
# my_dict = {a_key:"hello", (1,2):5}
# my_dict[5] = "Armenia"
# print(my_dict)
# my_dict[5] = "Ani"
# print(my_dict)

# for key in my_dict:
# 	print("key", key, "value", my_dict[key])

# dict_1 = {"key1":1, "key2":2}
# dict_2 = {"key1":10, "key3":1, "key4":2}
# dict_3 = {}
# # for i in dict_1:
# # 	dict_3[i] = dict_1[i]
# # for j in dict_2:
# # 	dict_3[j] = dict_2[j]
# # print(dict_3)
# # # secondversion
# # dict_1 = {"key1":1, "key2":2}
# # dict_2 = {"key1":10, "key3":1, "key4":2}
# # for key in dict_1:
# # 	dict_2[key] = dict_1[key]
# # print(dict_1)
# # print(dict_2)

# list_dict = [dict_1,dict_2,dict_3]
# for new_dict in list_dict:
# 	for key in new_dict:
# 		dict_3[key] = new_dict[key]


dict_1 = {"key1":1, "key2":2}
dict_2 = {"key1":10, "key3":1, "key4":2}


# dict_2["key4"] = dict_2.pop("key4")
# dict_2.pop("key4")
# print(dict_2)
# dict_2["key1"] = 50
# dict_2.popitem()
# print(dict_2)

dict_1.update(dict_2)
print(dict_1)








