n = int(input())
k = 1
for i in range(1,11):
    k*=i
    if n<=k:
        print(i)
        break