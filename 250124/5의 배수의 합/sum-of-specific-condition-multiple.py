inp = input().split()
a = int(inp[0])
b = int(inp[1])
c = 0
if b>=a:    
    for i in range(a,b+1):
        if i%5==0:
            c+=i
    print(c)
else:
    for i in range(b,a+1):
        if i%5==0:
            c+=i
    print(c)