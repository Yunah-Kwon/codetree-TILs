n = int(input())
k = 0

for i in range(1,101):
    k+=i
    if n <= k:
        print(i)
        break