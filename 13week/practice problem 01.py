def selectionSort(ary):
    n = len(ary)
    for end in range(1, n):
        for cur in range(end, 0, -1):
            if (ary[cur - 1][1] > ary[cur][1]):
                ary[cur - 1], ary[cur] = ary[cur], ary[cur - 1]
    return ary


ary = [['선미', 88], ['초아', 99], ['화사', 71], ['영탁', 78], ['영웅', 67], ['민호', 92]]

print('정렬 전 -->', ary)

selectionSort(ary)
print('정렬 후 -->', ary)

print('## 성젹별 조 편성표 ##')

for i in range(len(ary) // 2):
    print(ary[i][0], ':', ary[len(ary) - i - 1][0])