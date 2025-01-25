inp = input().split()
a = int(inp[0])
b = int(inp[1])
c = a

if b>0:
    for i in range(1,b):
        a*=c
    print(a)