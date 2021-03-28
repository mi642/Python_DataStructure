def add_data(friend):
    katok.append(None)
    klen = len(katok)
    katok[klen - 1] = friend

def insert_data(position, friend):
    if position < 0 or position + 1 > len(katok):
        print("데이터를 삽입할 범위를 벗어났습니다.")
        return

    katok.append(None)
    kLen = len(katok)

    for i in range(kLen - 1, position, -1):
        katok[i] = katok[i - 1]
        katok[i - 1] = None

    katok[position] = friend

def delete_data(position):
    if position < 0 or position + 1 > len(katok):
        print("데이터를 삭제할 범위를 벗어났습니다.")
        return

    klen = len(katok)
    katok[position] = None

    for i in range(position + 1, klen):
        katok[i - 1] = katok[i]
        katok[i] = None

    del (katok[klen - 1])

katok = []
select = -1


if __name__ == "__main__":
    while (select != 4):
        select = int(input("선택하세요 (1 : 추가, 2 : 삽입, 3 : 삭제, 4 : 종료) --> "))

        if (select == 1):
            data = input("추가할 데이터 --> ")
            add_data(data)
            print(katok)
        elif (select == 2):
            position = int(input("삽입 할 위치 --> "))
            data = input("추가할 데이터 --> ")
            insert_data(position, data)
            print(katok)
        elif (select == 3):
            position = int(input("삭제할 위치 --> "))
            delete_data(position)
            print(katok)
        elif (select == 4):
            print(katok)
            exit
        else:
            print("1~4 중 하나를 입력하세요.")
            continue