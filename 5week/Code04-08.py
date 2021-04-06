class Node():
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start):
    current = start
    if current == None:
        return
    print(current.data, end = ' ')

    while current.link != None:
        current = current.link
        print(current.data, end = ' ')
    print()

def finaNode(findData):
    global memory, head, current, pre
    current = head

    if current.data == findData:
        return current

    while current.link != None:
        current = current.link

        if current.data == findData:
            return current
    return Node()

memory = []
head, current, pre = None, None, None
dataArray = ["다현", "정연", "쯔위", "사나", "지효"]

if __name__ == "__main__" :
    node = Node()
    node.data = dataArray[0]
    head = node
    memory.append(node)

    for data in dataArray[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        memory.append(node)

    printNodes(head)

    fNode = finaNode("다현")
    print(fNode.data)

    fNode = finaNode("쯔위")
    print(fNode.data)

    fNode = finaNode("재남")
    print(fNode.data)