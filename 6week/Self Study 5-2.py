import random

class Node():
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start):
    current = start
    if current.link == None:
        return
    print(current.data, end = ' ')
    while current.link != start:
        current = current.link
        print(current.data, end = ' ')
    print()

def countOddEven():
    global memory, head, current, pre

    p, m = 0, 0
    if head == None:
        return False

    current = head
    while True:
        if current.data > 0:
            p += 1
        elif current.data == 0:
            continue
        else:
            m += 1
        if current.link == head:
            break
        current = current.link

    return p, m

def makeZeroNumber(p, m):

    current = head
    while True:
        if current.data != 0:
            current.data *= -1
        if current.link == head:
            break
        current = current.link


memory = []
head, current, pre = None, None, None

if __name__ == "__main__":

    dataArray = []
    for _ in range(7):
        dataArray.append(random.randint(-100, 100))

    node = Node()
    node.data = dataArray[0]
    head = node
    node.link = head
    memory.append(node)

    for data in dataArray[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        node.link = head
        memory.append(node)

    printNodes(head)

    pCount, mCount = countOddEven()
    print("양수 -->", pCount, "\t", "음수 -->", mCount)

    makeZeroNumber(pCount, mCount)
    printNodes(head)