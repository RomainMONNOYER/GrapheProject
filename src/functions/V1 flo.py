from functions.lecture import *
import math

if __name__ == '__main__':
    N, E, B, quantities = readData("datas/data1.dat")
    sol = []
    print(N, E, B, quantities)
    # base = int(sum(quantities)/(B * E))
    base = quantities[-1]

    val = [x // base for x in quantities]
    rest = [x % base for x in quantities]

    pack = sum(val)
    average = math.ceil(pack/(B * E))
    print(len(rest),rest)

    #Box 1 with maximum value (multiple of base)
    v1 = (pack - (B-2) * E) * base // E
    r1 = (pack - (B-2) * E) * base % E
    temp = []
    for i in range(r1):
        temp.append(v1)
    for i in range(E-r1):
        temp.append(v1 - base)
    sol.append(temp)

    #Bax 2 .. B-1 of base
    for i in range(B-2):
        temp = []
        for j in range(E):
            temp.append(base)
        sol.append(temp)

    #Box B with rest
    sol.append(sorted(rest,reverse=True))

    print("\nSolution :\n")
    for i in range(B):
        print(sol[i])

    print("\n\nValue :")
    print(sum([sol[i][0] for i in range(B)]))


    print("\n\nVerif :")
    print(sum([sum([x for x in j]) for j in sol]))
    print(sum([sum([x for x in j]) for j in quantities]))





