inp = input().split()
a = int(inp[0])
b = int(inp[1])
c = 0
sum_val = 0

for i in range(a,b+1):
    if i %5==0 or i%7==0:
        sum_val +=i
        c +=1
print(sum_val, end = " ")
print(f"{sum_val/c:.1f}")