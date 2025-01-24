n = int(input())
cnt = 0

for i in range (n):
    inp = int(input())
    if inp%2==1 and inp%3==0:
        cnt+=inp
print(cnt)