def selectionSort(ary):
    n = len(ary)
    for end in range(1, n):
        for cur in range(end, 0, -1):
            if (ary[cur - 1] > ary[cur]):
                ary[cur - 1], ary[cur] = ary[cur], ary[cur - 1]
    return ary

before = [[55, 33, 250, 44], [88, 1, 76, 23], [199, 222, 38, 47], [155, 145, 20, 99]]
after = []

for i in range(len(before)):
    for k in range(len(before[i])):
        after.append(before[i][k])

print('1차원 변경 후, 정렬 전 -->', after)
after = selectionSort(after)
print('1차원 변경 후, 정렬 후 -->', after)

print('중앙값 -->', after[len(after) // 2])