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

strs = ['진', '달', '래', '꽃', '\n', '나', ' ', '보', '기', '가', ' ', '역', '겨', '워', '\n', '가', '실', ' ', '때', '에', '는', '\n', '말', '없', '이', ' ', '고', '이', ' ', '보', '내', '드', '리', '오', '리', '다', '.']
SIZE = len(strs)
stack = [None for _ in range(SIZE)]
top = -1

if __name__ == "__main__":

    print("----원본----")
    for str in strs:
        push(str)
        print(str, end = '')
    print("")

    print("----거꾸로 처리된 결과----")
    while True:
        str = pop()
        if (str == None):
            break
        print(str, end = '')
    print("")