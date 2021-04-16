def isStackFull():
    global SIZE, stack, top
    if (top >= SIZE - 1):
        return True
    else:
        return False

def isStackEmpty():
    global SIZE, stack, top
    if (top == -1):
        return True
    else:
        return False

def push(data):
    global SIZE, stack, top
    if (isStackFull()):
        #print("스택이 꽉 찼습니다.")
        return
    top += 1
    stack[top] = data

def pop():
    global SIZE, stack, top
    if (isStackEmpty()):
        #print("스택이 비었습니다.")
        return None
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

def peek():
    global SIZE, stack, top
    if (isStackEmpty()):
        #print("스택이 비었습니다.")
        return None
    return stack[top]


SIZE = 7
stack = [None for _ in range(SIZE)]
top = -1

if __name__ == "__main__":
    colors = ['주황', '초록', '파랑', '보라', '빨강', '노랑']

    print("과자집에 가는 길", end = " : ")
    for color in colors:
        push(color)
        print(color, end = ' --> ')
    print("과자집")

    print("우리집에 오는 길", end = " : ")
    while True:
        color = pop()
        if (color == None):
            break
        print(color, end = ' --> ')
    print("우리집")