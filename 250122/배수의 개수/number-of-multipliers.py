cnt_3 = 0
cnt_5 = 0
for i in range(10):
    inp = int(input())
    if inp % 3 == 0:
        cnt_3 += 1
    if inp % 5==0 :
        cnt_5 += 1

# 루프가 끝난 후 한 번만 출력
print(cnt_3, end=" ")
print(cnt_5)
