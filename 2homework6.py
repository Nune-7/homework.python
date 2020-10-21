import os
print("This file is running from", os.getcwd())

print(os.listdir(f"{os.getcwd()}/."))

base_dir = os.getcwd()
os.makedirs(f"{base_dir}/./Dir1/Dir2")
os.chdir("/Users/User/Desktop/python/Dir1")
print("we are now in {}".format(os.getcwd()))
os.makedirs(f"{base_dir}/./Dir1/Dir3/Dir4")

# ex2
base_dir = os.getcwd()
print("we are now in {}".format(os.getcwd()))
os.chdir("/Users/User/Desktop/python/Dir1")
print("we are now in {}".format(os.getcwd()))
print(os.listdir())
a = input("Do you like to delete the created folders?\n")

while a == "yes":
	b = os.getcwd()
	c = os.chdir("/..")
	print(os.rmdir(b))
else:
	pass

