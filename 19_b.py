print("First Case: ")
i=1
while i<101 :
	if i%2!=0:
		pass
	elif i==90:
		break
	else:
		print(i,end=" ")
	i+=1
print()

print("Second Case: ")
i=1
while i<101:
	if i%2!=0:
		pass
	elif i/10 in [6,7,8,9]:
		i+=1
		continue
	else:
		print(i,end=" ")
	i+=1
print()
