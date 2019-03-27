print("First Case: ")
for i in range(1,101):
	if i%2!=0:
		pass
	elif i==50:
		break
	else:
		print(i,end=" ")
print()

print("Second Case: ")
for i in range(1,101):
	if i%2!=0:
		pass
	elif i/10 in [1,2,3,4,5]:
		continue
	else:
		print(i,end=" ")
print()
