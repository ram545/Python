
def isPrime(n):
	if n==2 or n==3 :
		return True
	if n%2==0 or n<2 :
		return False
	for i in range(3,int(n**0.5)+1,2):
		if n%i==0 :
			return False

	return True


A = int(input("Enter a number: "))
if isPrime(A):
	print(A,"is a prime number")
else :
	print(A,"is not a prime number")
