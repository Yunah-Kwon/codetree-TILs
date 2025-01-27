a = int(input())

for i in range(1,a+1):
    if (i%2==0 and i%4!=0) or i//8==0 or i//8==2 or i//8==4 or i//8==6 or i//8==8 or i//8==10 or i//8==10 or i//8==12 or i%7<4:
        continue
    print(i, end =" ") 