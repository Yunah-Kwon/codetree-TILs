arr_a = input().split()
arr_b = input().split()

m_a = int(arr_a[0])
e_a = int(arr_a[1])
m_b = int(arr_b[0])
e_b = int(arr_b[1])

if m_a>m_b:
    print("A")
elif m_b>m_a:
    print("B")
else: #수학점수 동일
    if e_a>e_b:
        print("A")
    else:
        print("B")
   

