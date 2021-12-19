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
    for i in range(5):
        print("\n============================================\nrecuit\n=========================================\n")
        begin = time.time()
        sol, decomp = recuit.run(N, B, E, quantities, sol, decomp, alpha = 0.93, epsilon = 10**-3)
        #printsol(sol, decomp)
        print("COST", sum([sol[i][0] for i in range(len(sol))]))
        print("\ntime:", end=' ')
        print(time.time() - begin)
    """




    while True:
        prevSol = sum([sol[i][0] for i in range(len(sol))])
        sol1, decomp1 = sol, decomp

        while True:
            sol2, decomp2 = sol1, decomp1
            print("\n============================================\ntabou\n=========================================\n")
            begin = time.time()
            sol2, decomp2 = tabou.run(N, B, E, quantities, sol2, decomp2)
            #printsol(sol1, decomp1)
            print("COST", sum([sol2[i][0] for i in range(len(sol2))]))
            print("\ntime:", end=' ')
            print(time.time() - begin)
            print(sum([sol1[i][0] for i in range(len(sol1))]))
            if sum([sol2[i][0] for i in range(len(sol2))]) == sum([sol1[i][0] for i in range(len(sol1))]):
                break
            if sum([sol2[i][0] for i in range(len(sol2))]) > sum([sol1[i][0] for i in range(len(sol1))]):
                break
            sol1, decomp1 = sol2, decomp2

        print("\n============================================\nrecuit\n=========================================\n")
        begin = time.time()
        sol1,decomp1 = recuit.run(N,B,E,quantities,sol1,decomp1)
        #printsol(sol2,decomp2)
        print("COST", sum([sol1[i][0] for i in range(len(sol1))]))
        print("\ntime:", end = ' ')
        print(time.time()-begin)

        print("\n============================================\nlocalSearch\n=========================================\n")
        begin = time.time()
        sol1,decomp1 = localSearch.run(N,B,E,quantities,sol1,decomp1)
        #printsol(sol1,decomp1)
        print("COST", sum([sol1[i][0] for i in range(len(sol1))]))
        print(prevSol)
        print("\ntime:", end = ' ')
        print(time.time()-begin)


        if sum([sol1[i][0] for i in range(len(sol1))]) == prevSol:
            print("No amelioration possible...")
            break
        if time.time() - TrueBegin > 300:
            print("Time Limit Exceed")
            break

        sol, decomp = sol1, decomp1

    printsol(sol1,decomp1)
    print("Total Run time: ", - TrueBegin + time.time())
    #To comment
    print(sum(quantities) == sum([sum([x for x in j]) for j in sol]))






