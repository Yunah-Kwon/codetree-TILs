inp = input()
arr = inp.split()
a,b,c = int(arr[0]),int(arr[1]), int(arr[2])

if a>b and a>c:
    print(a)
elif a>b and a<c:
    print(c)
elif b>a and b>c:
    print(b)
elif b>a and b<c:
    print(c)
else:
    print(c)

