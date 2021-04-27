list = []
count = 1

for i in range(0, 12):
    list.append(i + 1)

for i in range(0, 3):
    for j in range(0, 4):
        if j != 3:
            print("%3d" %list[count - 1], end = '')
        else:
            print("%3d" %list[count - 1])
        count += 1