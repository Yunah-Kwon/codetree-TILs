inp = input().split()
a = int(inp[0])
b = int(inp[1])
c = 0

for i in range(a,b+1):
    if i%2==0:
        c+=i
print(c)