class Node():
    def __init__(self):
        self.data = None
        self.forward = None
        self.backward = None

def printNodes(start):
    current = start
    if current.backward == None:
        return

    print(current.data, end = " ")
    while current.backward != None:
        current = current.backward
        print(current.data, end = " ")
    print()

    print(current.data, end=" ")
    while current.forward != start:
        current = current.forward
        print(current.data, end=" ")
    current = current.forward
    print(current.data, end=" ")

def findNode(findData):
    global memory, head, current, pre
    current = head

    if current.data == findData:
        return

    while current.backward != None:
        current = current.backward

        if current.data == findData:
            return
    return False


memory = []
head, current, pre = None, None, None
data = []

if __name__ == "__main__":
    for i in range(0, 5):
        name = input()
        data.append(name)

    node = Node()
    node.data = data[0]
    head = node
    memory.append(node)

    for data in data[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.backward = node
        node.forward = pre
        memory.append(node)

    find = input()
    if findNode(find) == False:
        print("X")
    else:
        printNodes(current)