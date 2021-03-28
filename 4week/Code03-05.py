def printPoly(p_x):
    term = len(p_x) - 1
    polyStr = "P(x) = "

    for i in range(len(p_x)):
        coef = p_x[i]

        if (coef >= 0):
            polyStr += "+"
        polyStr += str(coef) + "x^" + str(term) + " "
        term -= 1

    return polyStr

def calPoly(xVal, p_x):
    retValue = 0
    term = len(p_x) - 1

    for i in range(len(p_x)):
        coef = p_x[i]
        retValue += coef * xVal ** term
        term -= 1

    return retValue


p_x = [7, -4, 0, 5]

if __name__ == "__main__":
    pStr = printPoly(p_x)
    print(pStr)

    xValue = int(input("X 값 --> "))

    pxValue = calPoly(xValue, p_x)
    print(pxValue)