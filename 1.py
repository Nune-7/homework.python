Employees = {
"emp1": {"name": "John", "salary":7500},
"emp2": {"name":"Emma", "salary": 8000}, 
"emp3": {"name": "Brad", "salary": 6500}}
average_s = (7500+8000+6500)//3
for i in Employees:
	Employees[i]["salary"] = average_s
print(Employees)
