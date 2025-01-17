inp = input()
arr = inp.split()
a,b,c = int(arr[0]),int(arr[1]), int(arr[2])

if a>=b:
    if a>=c:
        print(a)
    else:
        print(c)
elif b>=a:
    if b>=c:
        print(b)
    else:
        print(c)
elif c>=a:
    if c>=b:
        print(c)
    else:
        print(b)

