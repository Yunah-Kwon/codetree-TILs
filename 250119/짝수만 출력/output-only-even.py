inp = input().split()
a = int(inp[0])
b = int(inp[1])

if a%2==0:
    while a <=b:
        print(a, end = " ")
        a+=2
else:
    a +=1
    while a <=b:
        print(a, end =" ")
        a+=2