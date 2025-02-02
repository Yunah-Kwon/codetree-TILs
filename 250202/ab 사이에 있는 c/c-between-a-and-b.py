inp = input().split()

a = int(inp[0])
b = int(inp[1])
c = int(inp[2])

s = False

for i in range(a,b+1):
    if i%c==0:
        s = True
if s == True:
    print("YES")
else:
    print("NO")

