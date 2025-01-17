inp_1 = input()
arr_1 = inp_1.split()
a_s, a_t = arr_1[0], int(arr_1[1])

inp_2 = input()
arr_2 = inp_2.split()
b_s, b_t = arr_2[0], int(arr_2[1])

inp_3 = input()
arr_3 = inp_3.split()
c_s, c_t = arr_3[0], int(arr_3[1])

test = []

if a_s=='Y':
    if a_t>=37:
        test.append("A")
    else:
        test.append("C")
elif a_s=='N':
    if a_t>=37:
        test.append("C")
    else:
        test.append("D")

if b_s=='Y':
    if b_t>=37:
        test.append("A")
    else:
        test.append("C")
elif b_s=='N':
    if b_t>=37:
        test.append("C")
    else:
        test.append("D")

if c_s=='Y':
    if c_t>=37:
        test.append("A")
    else:
        test.append("C")
elif c_s=='N':
    if c_t>=37:
        test.append("C")
    else:
        test.append("D")

if test.count('A') >=2:
    print("E")
else:
    print("N")