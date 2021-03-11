##함수 선언 부분##
def multi(v1, v2):
    retlist = []
    rest1 = v1 + v2
    rest2 = v1 - v2
    rest3 = v1 * v2
    rest4 = v1 // v2
    rest5 = v1 % v2
    rest6 = 1
    for i in range(0, v2):
        rest6 *= v1
    retlist.append(rest1)
    retlist.append(rest2)
    retlist.append(rest3)
    retlist.append(rest4)
    retlist.append(rest5)
    retlist.append(rest6)
    return retlist

##전역 변수 부분##
mylist = []
plus, sub, mul, quo, rem, squ = 0, 0, 0, 0, 0, 0

##메인 코드 부분##
mylist = multi(100, 20)
plus = mylist[0]
sub = mylist[1]
mul = mylist[2]
quo = mylist[3]
rem = mylist[4]
squ = mylist[5]

print("multi()에서 반환한 값 ==> %d, %d, %d, %d, %d, %d" % (plus, sub, mul, quo, rem, squ))
