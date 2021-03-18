import random

print("로또 번호 생성을 시작합니다.")
num = int(input("몇 번을 뽑을까요? "))

list = [num for num in range(1, 46)]

for i in range(0, num):
    l = random.sample(list, 6)
    l.sort()
    print("자동번호-->", l[0], l[1], l[2], l[3], l[4], l[5])