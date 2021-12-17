from ..Splitter.smartDecreasing import *

def run(N,B,E,quantities,sol,decomp):
    base = [x[0] for x in sol]
    value = sum(base)
    step = 1
    V = [True]

    while V:
        V = []
        for i in range(B):
            tempbase = [x for x in base]
            tempbase[i] -= step
            tempsol,tempdecomp = evaluate(N,B,E,quantities,tempbase,B-1)

            if tempsol:
                cost = sum([sol[i][0] for i in range(len(tempsol))])
                V.append((cost,tempsol,tempdecomp,tempbase))

        V = [x for x in V if x[0] <= value]
        if V:
            V.sort(key=lambda x:x[0])
            cost = V[0][0]
            if cost <= value :
                sol,decomp = V[0][1],V[0][2]
                value = V[0][0]
                base = V[0][3]


    return sol,decomp





