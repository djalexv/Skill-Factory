K = float(input("Ждем K - ")) #float(10)
A = [float(_) for _ in range(21)]
mid = len(A) // 2
low = 0
high = len(A) - 1
s = 0
Tstr = "K - Вне массива"
EndStr = "Номер позиции элемента, который меньше K = "
if K < A[0]:
    EndStr = Tstr
elif K > A[high]:
    s = high
    EndStr = Tstr + ', но ' + EndStr + str(s)
else:
    while low <= high:
        if A[mid] == K:
            if mid != 0:
                s = mid-1
                EndStr = EndStr + str(s)
            else:
                s = mid
                EndStr = "Элемент, который меньше K, в массиве отсутсвует, так К имеет индекс - " + str(s)
            break
        elif A[mid] < K <= A[mid + 1]:
            s = mid
            EndStr = EndStr + str(s)
            break
        elif K > A[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2
print(EndStr)
