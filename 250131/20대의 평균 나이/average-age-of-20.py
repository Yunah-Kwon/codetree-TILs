k = 0
m = 0
while True:
    n = int(input())
    if n//10==2:
        k+=n
        m+=1
    else:
        break
print(f'{k/m:.2f}')