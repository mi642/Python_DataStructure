list = []

for i in range(0, 12):
    list.append(i + 1)

for i in range(0, 12):

    if (i + 1) % 4 == 0 & i != len(list):
        print("%3d" % list[i])
    else:
        print("%3d" % list[i], end='')