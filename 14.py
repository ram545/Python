A = [1,2,3,4,5,6,7,8,9,10,11]
B = ["Rama","Krishna","Reddy","Ashish","Chandana","Dinesh","Pavan","Praneeth","Vikash","Dev","Tanay"]

print("The list is: ",B)

for i in range(2):
	index = int(input("Enter a index: "))
	print(A[index-1]," : ",B[index-1])

print("The names in range 4 to 9 are: ",B[4:10])

print("The names in range 3 to end are: ",B[3:])

print("The list of names repeated 2 times: ")

print(B*2)

print("The concatenation of Lists is: ",A+B)


for i in range(11):
	print(A[i],"  ::  ",B[i])

