lst=["Rama","Krishna","Reddy","Ashish","Chandana"]


if("Reddy" in lst) :
	print("Reddy is in the list: ",lst)

for i in range(len(lst)):
	if(lst[i]=="Reddy"):
		print("Reddy is in list at index: ",i)

print("The list in reverse: ",lst[::-1])
