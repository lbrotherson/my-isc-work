forward = list()
backward = list()
values = ["a","b","c"]
for i in values:
	forward.append(i)
	backward.insert(0,i)
print(forward)
print(backward)
forward.reverse()
print(forward)
if forward == backward:
	print("True")
else:
	print("WRONG")
	
	
	
