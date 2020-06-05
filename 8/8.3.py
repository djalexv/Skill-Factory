#
# R = [i + 3 for i in range(11)]
# print(R, len(R))
#
# for i in range(6):
#     # print(i)
#     S = R[i]
#     R[i] = R[10 - i]
#     R[10 - i] = S
#
# print(R)

Y = input().split()
Y = list(map(int, Y))
print(Y)
for i in range(1, len(Y)):
    b = Y[i]
    j = i-1
    while (j >= 0) and (b < Y[j]):
        Y[j+1] = Y[j]
        j-=1
    Y[j+1] = b
print(Y)