def seqSearch(ary, fData):
    global position
    pos = -1
    size = len(ary)

    for i in range(size):
        if (ary[i] == fData):
            pos = i
            position.append(pos)
    return pos


dataAry = [188, 50, 150, 168, 50, 162, 105, 120, 177, 50]
findData = 50
position = []
pos = - 1

print("배열 -->", dataAry)

pos = seqSearch(dataAry, findData)

if (pos == -1):
    print(findData, "(이)가 없네요.")
else:
    print(findData, "(은)는 ", position, "위치에 있음")