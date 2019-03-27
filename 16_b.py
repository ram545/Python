def seiveOfErathoneses(N):
	g = [1]*(N+1)
	g[0]=g[1]=0
	for i in range(2,int((N+1)**0.5)+1):
		if g[i]==1:
			for p in range(2*i,N+1,i):
				if g[p]==1:
					g[p]=0

	for i in range(1,(N+1)):
		if g[i]==1:
			print(i,end=" ")

	print()


a = int(input("Enter a number: "))
seiveOfErathoneses(a)