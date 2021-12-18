import random
from ..Splitter.modular import *


def run(N,B,E,quantities,sol,decomp):
    # Setup s
    base = [x[0] for x in sol]
    value = sum(base)
    step = 1
    T = 100
    alpha = 0.9
    epsilon = 1
    V = [True]

    while T >= epsilon: # While enought hot
        V = []
        for i in range(B): # Evaluate each canonic variation of the base (positive and negative)
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

        if V:   # Select random with weights
            selected = random.choices(V,weights=(2**((value - x[0])/T) for x in V))[0]

            if selected[0] <= value or random.random() < 2**((value - selected[0])/T): # Attribute if better or lucky
                sol,decomp = selected[1],selected[2]
                value = selected[0]
                base = [x[0] for x in sol]

        # Update heat
        T *= alpha


    return sol,decomp





