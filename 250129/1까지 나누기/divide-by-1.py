n = int(input())

for i in range(1,n+1):
    n//=i
    if n==0:
        print(i)
        break
