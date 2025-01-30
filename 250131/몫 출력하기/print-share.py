k = 0

while True:
    n = int(input())
    if n%2!=0:
        continue
    a = n//2
    print(a)
    k+=1
    if k==3:
        break