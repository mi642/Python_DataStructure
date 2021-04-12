class Node():
    def __init__(self):
        self.data = None
        self.forward = None
        self.backward = None

def printNodes(start):
    current = start
    if current.backward == None:
        return

    print("정방향 -->", end = " ")
    print(current.data, end = " ")
    while current.backward != None:
        current = current.backward
        print(current.data, end = " ")
    print()

    print("역방향 -->", end = " ")
    print(current.data, end=" ")
    while current.forward != None:
        current = current.forward
        print(current.data, end=" ")


memory = []
head, current, pre = None, None, None
dataArray = ["다현", "정연", "쯔위", "사나", "지효"]

if __name__ == "__main__":
    node = Node()
    node.data = dataArray[0]
    head = node
    memory.append(node)

    for data in dataArray[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.backward = node
        node.forward = pre
        memory.append(node)

    printNodes(head)