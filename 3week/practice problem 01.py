import random

print("로또 번호 생성을 시작합니다.")
num = int(input("몇 번을 뽑을까요? "))

for i in range(0, num):
    list = []
    print("자동번호 -->", end = " ")
    for j in range(0, 6):
        rand_num = random.randint(1, 45)
        while rand_num in list:
            rand_num = random.randint(1, 45)
        list.append(rand_num)

    list.sort()
    for j in range(0, 6):
        print(list[j], end = " ")

    print()