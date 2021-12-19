from ..Splitter.adaptative import *
import itertools

def run(N,B,E,quantities,sol,decomp):
    # Setup s
    base = [x[0] for x in sol]
    value = sum(base)
    step = 1
    V = [True]

    while V: # While neightbour are smaller or equal
        V = []
        lst = list(itertools.product([0, 1], repeat=B))

        for vec in [list(x) for x in lst[1:]]: # Evaluate each neightbour
            tempbase = [x for x in base]
            for i in range(B):
                tempbase[i] -= vec[i]
            tempsol,tempdecomp = evaluate(N,B,E,quantities,tempbase,B-2)

            if tempsol:
                cost = sum([tempsol[i][0] for i in range(len(tempsol))])
                if cost <= value and cost <= sum(tempbase): # Store if value is equal or best
                    V.append((cost,tempsol,tempdecomp,[x[0] for x in tempsol]))

            tempbase = [x for x in base]
            for i in range(B):
                tempbase[i] += vec[i]
            tempsol, tempdecomp = evaluate(N, B, E, quantities, tempbase, B - 2)

            if tempsol:
                cost = sum([tempsol[i][0] for i in range(len(tempsol))])
                if cost <= value and cost <= sum(tempbase):  # Store if value is equal or best
                    V.append((cost, tempsol, tempdecomp, [x[0] for x in tempsol]))

        if V:
            V.sort(key=lambda x:x[0])
            cost = V[0][0]
            if cost <= value and V[0][3] != base: # Replace by best
                sol,decomp = V[0][1],V[0][2]
                value = V[0][0]
                base = V[0][3]
            else:
                break


    return sol,decomp





