n = int(input())
k = 0

#n%i==0이면 i는 n의 약수
for i in range(1,n):
    if n%i==0:
        k+=i
if k==n:
    print("P")
else:
    print("N")
