average=0
lst = []
print("Enter 10 numbers: ")
for i in range(10):
	lst.append(int(input())
	average=average+lst[i]

avrg/=10

print("The numbers less than average: ")
for i in range(10):
	if lst[i]<avrg:
		print(lst[i],end=" ")


print("The numbers greater than average: ")
for i in range(10):
	if lst[i]>avrg:
		print(lst[i],end=" ")


print("The numbers equal to average: ")
for i in range(10):
	if lst[i]==avrg:
		print(lst[i],end=" ")


