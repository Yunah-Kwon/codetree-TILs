inp = input().split()

a = int(inp[0])
b = int(inp[1])
c = int(inp[2])
s = True

for i in range(a,b+1):
    if i%c==0:
        s = False

if s == False:
    print("NO")
else:
    print("YES")