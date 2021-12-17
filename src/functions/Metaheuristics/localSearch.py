from ..Splitter.modular import *

def run(N,B,E,quantities,sol,decomp):
    base = [x[0] for x in sol]
    value = sum(base)
    step = 1
    V = [True]

    while V:
        V = []
        for i in range(B):
            tempbase = base
            tempbase[i] -= step
            tempsol,tempdecomp = evaluate(N,B,E,quantities,tempbase,3)

            if tempsol:
                cost = sum([sol[i][0] for i in range(len(tempsol))])
                V.append((cost,tempsol,tempdecomp))

        if V and cost <= value:
            V.sort(key=lambda x:x[0])
            sol,decomp = V[0][1],V[0][2]
            value = V[0][0]
            base = [x[0] for x in sol]


    return sol,decomp




