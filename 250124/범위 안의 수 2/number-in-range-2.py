n = 0
k = 0
for i in range(10):
    a = int(input())
    if a>=0 and a<=200:
        n+=a
        k+=1
print(n, end = " ")
print(f"{n/k:.1f}")