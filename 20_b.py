import sys
lst = []
lst.append(0)
lst.append(1)

def genFebonnaci(N):
		lst.append(lst[N-1]+lst[N-2])
		if(lst[N]<sys.maxsize):
			genFebonnaci(N+1)
		else:
			lst.pop()

genFebonnaci(2)
print (lst)