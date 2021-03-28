def printPoly(list):
    polyStr = "P(x) = "

    for i in range(len(list)):
        term = list[i][0]
        coef = list[i][1]

        if (coef >= 0):
            polyStr += "+"
        polyStr += str(coef) + "x^" + str(term) + " "

    return polyStr

def calPoly(xVal, mylist):
    retValue = 0

    for i in range(len(mylist)):
        term = mylist[i][0]
        coef = mylist[i][1]
        retValue += coef * xVal ** term
        term -= 1

    return retValue


mylist = [[300, 7], [20, -4], [0, 5]]

if __name__ == "__main__":
    pStr = printPoly(mylist)
    print(pStr)

    xValue = int(input("X 값 --> "))

    pxValue = calPoly(xValue, mylist)
    print(pxValue)