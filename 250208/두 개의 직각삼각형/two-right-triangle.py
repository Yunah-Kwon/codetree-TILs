n = int(input())

for i in range(n):
    for j in range(n-i):
        print("*", end ="")
    for k in range(i):
        print(" ", end="")
    for a in range(i):
        print(" ", end ="")
    for b in range(n-i):
        print("*", end ="")
    print("")

