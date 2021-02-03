lst = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

sum1 = 0
sum2 = 0

for els in lst:
    sum2 += sum(els)
    for el in els:
        sum1 += el
        #print(el, end=' ')
    print(els, end=' ')
    print()

print(sum1)
print(sum2)
