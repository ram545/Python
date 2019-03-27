N = int(input("Enter the number of elements: "))
lst = []
print("Enter the numbers: ")
for i in range(N):
	lst.append(int(input()))

print("biggest: ",max(lst))
print("smalles: ",min(lst))