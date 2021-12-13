import math

def base(B,E,quantities):
    sol = []
    base = int(sum(quantities) / (B * E))
    if base > quantities[-1]:
        base = quantities[-1]

    val = [x // base for x in quantities]
    rest = [x % base for x in quantities]

    pack = sum(val)
    print("len(rest),rest : ",len(rest),rest)

    #Box 1 with maximum value (multiple of base)
    v1 = math.ceil((pack - (B-2) * E)/ E) * base
    print("pack,v1 : ",pack,v1)
    r1 = (pack - (B-2) * E) % E
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
    #sol.append(sorted(rest,reverse=True))
    sol.append(rest)

    print("\nSolve :\n")
    for i in range(B):
        print(sol[i])

    for i in range(len(val)):
        print("B{} :".format(i+1),val[i],rest[i])

    print("\n\nValue :")
    print(sum([sol[i][0] for i in range(B)]))

    print("\n\nVerif :")
    print("Init : ", sum(quantities))
    print("Sol : ", sum([sum([x for x in j]) for j in sol]))

    return sol,val,rest




