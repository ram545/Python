def genFebonnaci(N):
	if N==1:
		return 0
	elif N==2:
		return 1
	else:
		return genFebonnaci(N-1)+genFebonnaci(N-2)

a = int(input("Enter a number: "))
lst = []
for i in range(a):
	lst.append(genFebonnaci(i+1))

print("The series is: ")

print(lst)