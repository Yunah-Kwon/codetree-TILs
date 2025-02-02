n = int(input())
s = False

if n>=2:
    for i in range(2,n):
        if n%i==0:
            s = True
if s == True:
    print('C')
else:
    print('N')