
a = []
for i in range(5):
	a.append(int(input("Enter a Number: ")))

if( a[0] > a[1] and a[0] > a[2] and a[0] > a[3] and a[0]>a[4] ):
	print(a[0],"is the biggest")
elif( a[1]>a[0] and a[1] > a[2] and a[1] > a[3] and a[1]>a[4] ):
	print(a[1],"is the biggest")
elif( a[2]>a[0] and a[2] > a[1] and a[2] > a[3] and a[2]>a[4] ):
	print(a[2],"is the biggest")
elif( a[3]>a[0] and a[3] > a[1] and a[3] > a[2] and a[3]>a[4] ):
	print(a[3],"is the biggest")
else:
	print(a[4],"is the biggest")
