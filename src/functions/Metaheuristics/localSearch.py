from ..Splitter.adaptative import *

def run(N,B,E,quantities,sol,decomp, step=1):
    # Setup s
    base = [x[0] for x in sol]
    value = sum(base)
    V = [True]

    while V: # While neightbour are smaller or equal
        V = []
        for i in range(B): # Evaluate each canonic variation of the base (negative)
            tempbase = [x for x in base]
            tempbase[i] -= step
            tempsol,tempdecomp = evaluate(N,B,E,quantities,tempbase,B-2)

            if tempsol:
                cost = sum([tempsol[i][0] for i in range(len(tempsol))])
                if cost <= value and cost <= sum(tempbase): # Store if value is equal or best
                    V.append((cost,tempsol,tempdecomp,[x[0] for x in tempsol]))

        if V:
            V.sort(key=lambda x:x[0])
            cost = V[0][0]
            if cost <= value : # Replace by best
                sol,decomp = V[0][1],V[0][2]
                value = V[0][0]
                base = V[0][3]


    return sol,decomp





