from ..Splitter.adaptative import evaluate as ad
from ..Splitter.smartDecreasing import evaluate as SD
from ..Splitter.random import evaluate as rdm
from ..Splitter.modular import evaluate as mdlr

def run(N,B,E,quantities,sol,decomp):
    # Setup s
    base = [x[0] for x in sol]
    value = sum(base)
    step = 1

    shakes = 0
    threshold = 50
    Nsplitter = 4


    while shakes < threshold: # While we've not changed splitter enought
        V = []

        for i in range(B): # Evaluate each canonic variation of the base (negative)
            tempbase = [x for x in base]
            tempbase[i] -= step
            # Evaluate is defined below
            tempsol, tempdecomp = evaluate(N, B, E, quantities, tempbase, shakes % Nsplitter)

            if tempsol:
                cost = sum([tempsol[i][0] for i in range(len(tempsol))])
                V.append((cost, tempsol, tempdecomp, tempbase))

            tempbase = [x for x in base]
            tempbase[i] += step
            # Evaluate is defined below
            tempsol, tempdecomp = evaluate(N, B, E, quantities, tempbase, shakes % Nsplitter)

            if tempsol:
                cost = sum([sol[i][0] for i in range(len(tempsol))])
                V.append((cost, tempsol, tempdecomp, tempbase))

        if V:   # If solution, take best
            V.sort(key=lambda x:x[0])
            cost = V[0][0]
            if cost < value : # if answer is best
                # Affect s' to s
                sol, decomp = V[0][1], V[0][2]
                value = V[0][0]
                base = V[0][3]
            else:
                shakes += 1

        else:
            shakes += 1

    return sol,decomp




def evaluate(N, B, E, quantities, tempbase, i):
    if i == 0:
        return ad(N, B, E, quantities, tempbase, 0)
    if i == 1:
        return SD(N, B, E, quantities, tempbase, 0)
    if i == 2:
        return rdm(N, B, E, quantities, tempbase, 0)
    if i == 3:
        return mdlr(N, B, E, quantities, tempbase, B-1)