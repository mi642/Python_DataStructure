def sort_list(inp_name, inp_count):

    for i in range(len(mylist)):
        if (mylist[i][1] <= inp_count):
            mylist.insert(i, (inp_name, inp_count))
            break
        elif (mylist[len(mylist) - 1][1] > inp_count):
            mylist.append((inp_name, inp_count))
            break

    return mylist


mylist = [("다현", 200), ("정연", 150), ("쯔위", 90), ("사나", 30), ("지효", 15)]

if __name__ == "__main__":
    while (True):
        inp_name = input("추가할 친구 --> ")
        inp_count = int(input("카톡 횟수 --> "))
        print(sort_list(inp_name, inp_count))

