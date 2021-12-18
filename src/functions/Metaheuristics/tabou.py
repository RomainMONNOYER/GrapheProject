from ..Splitter.smartDecreasing import *

def run(N,B,E,quantities,sol,decomp):
    # Setup s
    base = [x[0] for x in sol]
    value = sum(base)
    V = [(value,sol,decomp,base)] # fake s' (= s)
    step = 1

    up = 0
    threshold = 2
    tabou = []
    N = 10

    while up < threshold: # While answer is not stuck for to long
        # Affect s' to s
        sol, decomp = V[0][1], V[0][2]
        value = V[0][0]
        base = V[0][3]

        # Update tabou list
        tabou.append(base)
        if len(tabou) > N:
            tabou.pop(0)

        V = []
        for i in range(B): # Evaluate each canonic variation of the base (negative)
            tempbase = [x for x in base]
            tempbase[i] -= step
            tempsol, tempdecomp = evaluate(N, B, E, quantities, tempbase, B - 1)

            if tempsol:
                cost = sum([sol[i][0] for i in range(len(tempsol))])
                if tempbase not in tabou:  # Store if base is not tabou
                    V.append((cost, tempsol, tempdecomp, tempbase))

            tempbase = [x for x in base]
            tempbase[i] += step
            tempsol, tempdecomp = evaluate(N, B, E, quantities, tempbase, B - 1)

            if tempsol:
                cost = sum([sol[i][0] for i in range(len(tempsol))])
                if tempbase not in tabou:  # Store if base is not tabou
                    V.append((cost, tempsol, tempdecomp, tempbase))

        if V:   # If solution, take best
            V.sort(key=lambda x:x[0])
            cost = V[0][0]
            if cost >= value : # if answer stuck
                up += 1

        else:
            print("Exit")
            break




    return sol,decomp





