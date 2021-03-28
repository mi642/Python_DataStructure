def printPoly(p_x):
    term = len(p_x) - 1
    polyStr = "P(x) = "

    for i in range(len(p_x)):
        coef = p_x[i]

        if (coef == 0):
            term -= 1
            continue
        elif (coef > 0 and term < len(p_x) - 1):
            polyStr += "+"
        polyStr += str(coef) + "x^" + str(term) + " "
        term -= 1

    return polyStr


p_x = [7, -4, 0, 5]

if __name__ == "__main__":
    pStr = printPoly(p_x)
    print(pStr)