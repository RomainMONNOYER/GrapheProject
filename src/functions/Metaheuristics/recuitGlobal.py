import random
import itertools
from ..Splitter.adaptative import *


def run(N,B,E,quantities,sol,decomp, alpha = 0.93, epsilon = 10**-1.5):
    # Setup s
    base = [x[0] for x in sol]
    value = sum(base)
    step = 1
    T = 100
    V = [True]

    while T >= epsilon: # While enought hot
        V = []
        lst = list(itertools.product([0, 1], repeat=B))

        for vec in [list(x) for x in lst[1:]]: # Evaluate each neightbour
            tempbase = base
            for i in range(B):
                tempbase[i] -= vec[i]
            tempsol,tempdecomp = evaluate(N,B,E,quantities,tempbase,3)

            if tempsol:
                cost = sum([tempsol[i][0] for i in range(len(tempsol))])
                V.append((cost,tempsol,tempdecomp))

            tempbase = base
            for i in range(B):
                tempbase[i] -= vec[i]
            tempsol, tempdecomp = evaluate(N, B, E, quantities, tempbase, 3)

            if tempsol:
                cost = sum([sol[i][0] for i in range(len(tempsol))])
                V.append((cost, tempsol, tempdecomp))

        if V:   # Select random with weights
            selected = random.choices(V,weights=(2**((value - x[0])/T) for x in V))[0]

            if selected[0] <= value or random.random() < 2**((value - selected[0])/T): # Attribute if better or lucky
                sol,decomp = selected[1],selected[2]
                value = selected[0]
                base = [x[0] for x in sol]

        # Update heat
        T *= alpha


    return sol,decomp





