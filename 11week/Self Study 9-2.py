class Graph():
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

G1 = None
stack = []
visitedAry = []
nameAry = ['문별', '솔라', '휘인', '쯔위', '선미', '화사']
문별, 솔라, 휘인, 쯔위, 선미, 화사 = 0, 1, 2, 3, 4, 5


G1 = Graph(6)
G1.graph[문별][솔라] = 1; G1.graph[문별][휘인] = 1;
G1.graph[솔라][문별] = 1; G1.graph[솔라][쯔위] = 1;
G1.graph[휘인][문별] = 1; G1.graph[휘인][쯔위] = 1;
G1.graph[쯔위][솔라] = 1; G1.graph[쯔위][휘인] = 1; G1.graph[쯔위][선미] = 1; G1.graph[쯔위][화사] = 1;
G1.graph[선미][쯔위] = 1; G1.graph[선미][화사] = 1;
G1.graph[화사][쯔위] = 1; G1.graph[화사][선미] = 1;

current = 0
stack.append(current)
visitedAry.append(current)

while (len(stack) != 0):
    next = None
    for vertex in range(6):
        if (G1.graph[current][vertex] == 1):
            if (vertex in visitedAry):
                pass
            else:
                next = vertex
                break

    if (next != None):
        current = next
        stack.append(current)
        visitedAry.append(current)
    else:
        current = stack.pop()


print('방문 순서 -->', end = '')
for i in visitedAry:
    print(nameAry[i], end = ' ')