n = int(input())
s = 0
c = 0

for i in range(n):
    a = int(input())
    s+=a
    c+=1
print(s, end = " ")
print(f"{s/c:.1f}")
