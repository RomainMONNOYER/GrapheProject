from functions.lecture import *
from functions.printSol import *
from src.functions.Base.BoxFiting import *
from functions.Splitter.smartIncreasing import *

import functions.Metaheuristics.localSearch as localSearch
import functions.Metaheuristics.recuit as recuit
import functions.Metaheuristics.tabou as tabou
import functions.Metaheuristics.SARtabou as SARtabou

import time

if __name__ == '__main__':
    best = [5243,8190,3897,9978,4966,15030,7194,239778,229428,226788]
    data = [{"id":i+1,"cost": 0, "time":0, "best":best[i]} for i in range(10)]

    for d in range(10):
        TrueBegin = time.time()
        N,B,E,quantities = readData("datas/data"+str(data[d]["id"])+ ".dat")
        sol,decomp = base(N,B,E,quantities)

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

                    print(
                        "\n============================================SAR-TABOU=========================================")

                    for i in range(20):
                        sol3, decomp3 = SARtabou.run(N, B, E, quantities, sol2, decomp2, minStep=1, maxStep=i + 1)
                        if sum([s[0] for s in sol3]) < sum([s[0] for s in sol2]):
                            sol2, decomp2 = sol3, decomp3

                    print("COST", sum([s[0] for s in sol2]))
                    print("time:", time.time() - begin)

                    if sum([s[0] for s in sol2]) >= Prev2:
                        break
                compteur = 0

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


                sol1, decomp1 = sol2, decomp2
                print(
                    "\n============================================LOCAL SEARCH=========================================")
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

        data[d]["cost"] = sum([s[0] for s in sol])
        data[d]["time"] = round(time.time() - TrueBegin, 3)
        data[d]["%"] = round((data[d]["cost"]-data[d]["best"])/data[d]["best"]*100,3)

    [print(d) for d in data]
