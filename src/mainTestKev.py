from functions.lecture import *
from functions.printSol import *
from src.functions.Base.BoxFiting import *
from functions.Splitter.smartIncreasing import *

import functions.Metaheuristics.localSearch as localSearch
import functions.Metaheuristics.recuit as recuit
import functions.Metaheuristics.tabou as tabou
import time

if __name__ == '__main__':
    TrueBegin = time.time()
    N,B,E,quantities = readData("datas/data10.dat")
    sol,decomp = base(N,B,E,quantities)

    printsol(sol,decomp)
    #print("COST", sum([sol[i][0] for i in range(len(sol))]))

    """
    for i in range(20):
        print("\n============================================\nrecuit\n=========================================\n")
        alpha = 0.99 - i/100
        print("aplha = ", alpha)
        begin = time.time()
        sol1, decomp1 = recuit.run(N, B, E, quantities, sol, decomp, alpha = alpha, epsilon = 10**-3)
        #printsol(sol, decomp)
        print("COST", sum([sol1[i][0] for i in range(len(sol1))]))
        print("\ntime:", end=' ')
        print(time.time() - begin)


    """
    while True:
        Prev = sum([s[0] for s in sol])
        sol1, decomp1 = sol, decomp
        while True:
            Prev1 = sum([s[0] for s in sol1])
            sol2, decomp2 = sol1, decomp1
            while True:
                Prev2 = sum([s[0] for s in sol2])
                sol3, decomp3 = sol2, decomp2
                begin = time.time()
                sol3, decomp3 = tabou.run(N, B, E, quantities, sol3, decomp3)

                print("\n============================================TABOU=========================================")
                print("COST",  sum([s[0] for s in sol3]))
                print("time:", time.time() - begin)

                if  sum([s[0] for s in sol3]) >= Prev2:
                    break
                sol2, decomp2 = sol3, decomp3

            print("\n============================================LOCAL SEARCH=========================================")
            begin = time.time()
            sol2, decomp2 = localSearch.run(N, B, E, quantities, sol2, decomp2)
            # printsol(sol1,decomp1)
            print("COST", sum([s[0] for s in sol2]))
            print("time:", end=' ')
            print(time.time() - begin)

            if sum([s[0] for s in sol2]) >= Prev1:
                break
            sol1, decomp1 = sol2, decomp2

        print("\n============================================RECUIT========================================")
        begin = time.time()
        sol1,decomp1 = recuit.run(N,B,E,quantities,sol1,decomp1)
        #printsol(sol2,decomp2)
        print("COST", sum([s[0] for s in sol1]))
        print("time:", time.time()-begin)



        if sum([s[0] for s in sol1]) >= Prev:
            print("No amelioration possible...")
            break

        if time.time() - TrueBegin > 300:
            print("Time Limit Exceed")
            break

        sol, decomp = sol1, decomp1

    printsol(sol,decomp)
    print("Total Run time: ", - TrueBegin + time.time())


