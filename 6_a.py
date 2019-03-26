
String=input("Enter a string: ")
length=len(String)
print(String[:])
print(String[::-1])
if length>2 :
	print(String[1:length-1])
if length>3 :
	print(String[2:length-1])
