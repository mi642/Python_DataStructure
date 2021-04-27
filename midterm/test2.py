class Node():
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(head):
    current = head

    if current == None:
        return
    print(current.data, end=' ')

    while current.link != None:
        current = current.link
        print(current.data, end=' ')
    print()

def findNode(findData):
    global memory, head, current, pre
    current = head

    if current.data == findData:
        deleteNode(findData)
        return

    while current.link != None:
        current = current.link

        if current.data == findData:
            deleteNode(findData)
            return
    return False

def deleteNode(deleteData):
    global memory, head, current, pre
    count = 0
    if head.data == deleteData:
        current = head
        for i in range(len(memory)):
            current.data = None
            pre = current
            current = current.link

        return

    current = head
    while current.link != None:
        pre = current
        current = current.link
        count += 1
        if current.data == deleteData:
            for i in range(len(memory) - count):
                current.data = None
                pre = current
                current = current.link
            return

memory = []
head, current, pre = None, None, None
data = []

if __name__ == "__main__" :
    for i in range(0, 6):
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
        pre.link = node
        memory.append(node)

    find = input()
    if findNode(find) == False:
        print("X")
    else:
        printNodes(head)