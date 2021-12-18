from ..Splitter.adaptative import *

def run(N,B,E,quantities,sol,decomp):
    # Setup s
    base = [x[0] for x in sol]
    value = sum(base)
    step = 1
    V = [True]

    while V: # While neightbour are smaller or equal
        V = []
        for i in range(B): # Evaluate each canonic variation of the base (negative)
            tempbase = [x for x in base]
            tempbase[i] -= step
            tempsol,tempdecomp = evaluate(N,B,E,quantities,tempbase,B-1)

            if tempsol:
                cost = sum([tempsol[i][0] for i in range(len(tempsol))])
                if cost <= value: # Store if value is equal or best
                    V.append((cost,tempsol,tempdecomp,tempbase))

        if V:
            V.sort(key=lambda x:x[0])
            cost = V[0][0]
            if cost <= value : # Replace by best
                sol,decomp = V[0][1],V[0][2]
                value = V[0][0]
                base = V[0][3]


    return sol,decomp





