inp = input().split()
b = int(inp[0])
a = int(inp[1])

for i in range(b,a-1,-2):
    if i%2==1:
        print(i, end =' ')