import math
a=int(input("Enter the number: "))
primeCheck=True
if(a<2):
	primeCheck=False
else:
	for i in range(2,math.floor(math.sqrt(a))+1):
		if(a%i==0):
			primeCheck=False
			break

if primeCheck:
	print(a,"is prime")
else:
	print(a,"is not prime")
