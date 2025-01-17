n = int(input())

#31일:1,3,5,7,(8,10,12)
#30일: 4,6,(9,11)
#28일: 2
if n%2==0 and n<=6:
    if n!=2:
        print("30")
    else:
        print("28")
elif n%2==0 and n>=8:
    print("31")
elif n%2!=0 and n<=7:
    print("31")
else:
    print("30")
