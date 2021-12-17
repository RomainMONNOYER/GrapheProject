import random
from ..Splitter.modular import *


def run(N,B,E,quantities,sol,decomp):
    base = [x[0] for x in sol]
    value = sum(base)
    step = 1
    T = 100
    alpha = 0.9
    epsilon = 50
    V = [True]

    while T >= epsilon:
        V = []
        for i in range(B):
            tempbase = base
            tempbase[i] -= step
            tempsol,tempdecomp = evaluate(N,B,E,quantities,tempbase,3)

            if tempsol:
                cost = sum([sol[i][0] for i in range(len(tempsol))])
                V.append((cost,tempsol,tempdecomp))

            tempbase = base
            tempbase[i] += step
            tempsol, tempdecomp = evaluate(N, B, E, quantities, tempbase, 3)

            if tempsol:
                cost = sum([sol[i][0] for i in range(len(tempsol))])
                V.append((cost, tempsol, tempdecomp))

        if V:
            selected = random.choices(V,weights=(2**(value - x[0]) for x in V))

            if selected[0] <= value or random.random() < 2**(value - selected[0]):
                sol,decomp = selected[1],selected[2]
                value = selected[0]
                base = [x[0] for x in sol]

        T *= alpha


    return sol,decomp




