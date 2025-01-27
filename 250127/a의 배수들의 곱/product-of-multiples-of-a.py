inp = input().split()

a = int(inp[0])
b = int(inp[1])
x = 1

for i in range (1,b+1):
    if i%a ==0:
        x*=i
print(x)