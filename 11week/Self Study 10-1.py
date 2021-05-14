def addNumber(largest, smallest):
    if (largest == smallest):
        return 1
    return largest + addNumber(largest - 1, smallest)


largest, smallest = 0, 0
A = int(input("숫자1-->"))
B = int(input("숫자2-->"))

if (A >= B):
    largest = A
    smallest = B
else:
    largest = B
    smallest = A

print(addNumber(largest, smallest))