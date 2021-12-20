from functions.lecture import *
from functions.printSol import *
from src.functions.Base.BoxFiting import *
from functions.Splitter.smartIncreasing import *

import functions.Metaheuristics.localSearchGlobal as localSearch
import functions.Metaheuristics.recuit as recuit
import functions.Metaheuristics.SARtabou as SARtabou
import functions.Metaheuristics.tabou as tabou

import time

def runPotion(N,B,E,quantities):
    TrueBegin = time.time()
    sol,decomp = base(N,B,E,quantities)

    print("============================================RECUIT=========================================")
    begin = time.time()
    sol, decomp = recuit.run(N, B, E, quantities, sol, decomp)
    #print("COST", sum([s[0] for s in sol]))
    #print("time:", time.time() - begin)

    while True:
        Prev = sum([s[0] for s in sol])
        sol1, decomp1 = sol, decomp
        while True:
            Prev1 = sum([s[0] for s in sol1])
            sol2, decomp2 = sol1, decomp1
            compteur = 0

            while True:
                compteur += 1
                Prev2 = sum([s[0] for s in sol2])
                begin = time.time()

                print("============================================SAR-TABOU=========================================")
                for _ in range(5):
                    prevBest = {"best": sum([s[0] for s in sol2]), "sol": sol2, "decomp": decomp2}
                    for i in range(10):
                        sol3, decomp3 = SARtabou.run(N, B, E, quantities, sol2, decomp2, minStep=1, maxStep=i + 1)
                        if sum([s[0] for s in sol3]) < prevBest["best"]:
                            prevBest = {"best": sum([s[0] for s in sol3]), "sol": sol3, "decomp": decomp3}

                    if prevBest["best"] < sum([s[0] for s in sol2]):
                        sol2, decomp2 = prevBest["sol"], prevBest["decomp"]

                #print("COST", sum([s[0] for s in sol2]))
                #print("time:", time.time() - begin)

                if sum([s[0] for s in sol2]) >= Prev2:
                    break
            compteur = 0

            while True:
                compteur += 1
                Prev2 = sum([s[0] for s in sol2])
                begin = time.time()

                print("============================================SAP-TABOU=========================================")

                for i in range(20):
                    sol3, decomp3 = tabou.run(N, B, E, quantities, sol2, decomp2, step=1 + i)
                    if sum([s[0] for s in sol3]) < sum([s[0] for s in sol2]):
                        sol2, decomp2 = sol3, decomp3

                #print("COST", sum([s[0] for s in sol2]))
                #print("time:", time.time() - begin)

                if sum([s[0] for s in sol2]) >= Prev2:
                    break

            sol1, decomp1 = sol2, decomp2
            print("============================================LOCAL SEARCH GLOBAL=========================================")
            begin = time.time()
            sol2, decomp2 = localSearch.run(N, B, E, quantities, sol1, decomp1, step=1)

            if sum([s[0] for s in sol2]) < sum([s[0] for s in sol1]):
                sol1, decomp1 = sol2, decomp2

            #print("COST", sum([s[0] for s in sol1]))
            #print("time:", time.time() - begin)

            if sum([s[0] for s in sol1]) >= Prev1:
                break

        if sum([s[0] for s in sol1]) >= Prev:
            print("No amelioration possible...")
            break

        if time.time() - TrueBegin > 300:
            print("Time Limit Exceed")
            break

        sol, decomp = sol1, decomp1

    printsol(sol, decomp)
    print("Total Run time: ", - TrueBegin + time.time())
    return sol, decomp, time.time() - TrueBegin