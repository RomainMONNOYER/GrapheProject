from functions.lecture import *
from functions.printSol import *
from src.functions.Base.BoxFiting import *
from functions.Splitter.smartIncreasing import *

import functions.Metaheuristics.localSearch as localSearch
import functions.Metaheuristics.recuit as recuit
import functions.Metaheuristics.tabou as tabou
import functions.Metaheuristics.SARtabou as SARtabou

import time
import random

if __name__ == '__main__':
    TrueBegin = time.time()
    N,B,E,quantities = readData("datas/data10.dat")
    sol,decomp = base(N,B,E,quantities)

    printsol(sol,decomp)
    #print("COST", sum([sol[i][0] for i in range(len(sol))]))

    """
    for i in range(20):
        step = i+1
        print("\nstep = ", step)
        sol1, decomp1 = sol, decomp
        costs = []
        begin = time.time()
        for _ in range(20):
            sol1, decomp1 = tabou.run(N, B, E, quantities, sol1, decomp1, step = step, threshold = 2)
            #printsol(sol, decomp)
            costs.append(sum([s[0] for s in sol1]))
        print("TIME: ", round(time.time() - begin,3), end = '\t\t')
        print("COST: ", min(costs))

    """
    while True:
        Prev = sum([s[0] for s in sol])
        sol1, decomp1 = sol, decomp
        while True:
            Prev1 = sum([s[0] for s in sol1])
            sol2, decomp2 = sol1, decomp1
            compteur = 0
            """
            while True:
                compteur += 1
                Prev2 = sum([s[0] for s in sol2])
                begin = time.time()

                print("\n============================================TABOU=========================================")

                for i in range(20):
                    sol3, decomp3 = tabou.run(N, B, E, quantities, sol2, decomp2, step = 1+i)
                    if sum([s[0] for s in sol3]) < sum([s[0] for s in sol2]):
                        sol2, decomp2 = sol3, decomp3

                print("COST",  sum([s[0] for s in sol2]))
                print("time:", time.time() - begin)

                if  sum([s[0] for s in sol2]) >= Prev2:
                    break
            """
            while True:
                compteur += 1
                Prev2 = sum([s[0] for s in sol2])
                begin = time.time()

                print("\n============================================SAR-TABOU=========================================")

                for i in range(20):
                    sol3, decomp3 = SARtabou.run(N, B, E, quantities, sol2, decomp2, minStep = 1, maxStep = i+1)
                    if sum([s[0] for s in sol3]) < sum([s[0] for s in sol2]):
                        sol2, decomp2 = sol3, decomp3

                print("COST",  sum([s[0] for s in sol2]))
                print("time:", time.time() - begin)

                if  sum([s[0] for s in sol2]) >= Prev2:
                    break

            sol1, decomp1 = sol2, decomp2
            print("\n============================================LOCAL SEARCH=========================================")
            begin = time.time()
            sol2, decomp2 = localSearch.run(N, B, E, quantities, sol1, decomp1, step=1)

            if sum([s[0] for s in sol2]) < sum([s[0] for s in sol1]):
                sol1, decomp1 = sol2, decomp2

            # printsol(sol1,decomp1)
            print("COST", sum([s[0] for s in sol1]))
            print("time:", end=' ')
            print(time.time() - begin)

            if sum([s[0] for s in sol1]) >= Prev1:
                break

        """
        print("\n============================================RECUIT========================================")
        begin = time.time()
        sol1,decomp1 = recuit.run(N,B,E,quantities,sol1,decomp1)
        #printsol(sol2,decomp2)
        print("COST", sum([s[0] for s in sol1]))
        print("time:", time.time()-begin)
        """


        if sum([s[0] for s in sol1]) >= Prev:
            print("No amelioration possible...")
            break

        if time.time() - TrueBegin > 300:
            print("Time Limit Exceed")
            break

        sol, decomp = sol1, decomp1

    printsol(sol,decomp)
    print("Total Run time: ", - TrueBegin + time.time())


