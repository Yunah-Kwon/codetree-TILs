inp = input().split()
a = int(inp[0])
b = int(inp[1])
c = a

for i in range(b-1):
    a*=c
print(a)