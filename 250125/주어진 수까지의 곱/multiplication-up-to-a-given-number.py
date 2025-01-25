inp = input().split()
a = int(inp[0])
b = int(inp[1])
p = 1

for i in range(a,b+1):
    p*=i
print(p)