from functions.lecture import *
from functions.printSol import *
from src.functions.Base.BoxFiting import *
from functions.Splitter.smartIncreasing import *

import functions.Metaheuristics.localSearch as localSearch
import functions.Metaheuristics.recuit as recuit
import functions.Metaheuristics.tabou as tabou
import time

if __name__ == '__main__':
    N,B,E,quantities = readData("datas/data10.dat")
    sol,decomp = base(N,B,E,quantities)

    printsol(sol,decomp)
    #print("COST", sum([sol[i][0] for i in range(len(sol))]))

    print("\n============================================\nlocalSearch\n=========================================\n")
    begin = time.time()
    sol1,decomp1 = localSearch.run(N,B,E,quantities,sol,decomp)
    printsol(sol1,decomp1)
    #print("COST", sum([sol1[i][0] for i in range(len(sol1))]))
    print("\ntime:", end = ' ')
    print(time.time()-begin)

    print("\n============================================\nrecuit\n=========================================\n")
    begin = time.time()
    sol2,decomp2 = recuit.run(N,B,E,quantities,sol,decomp)
    printsol(sol2,decomp2)
    #print("COST", sum([sol2[i][0] for i in range(len(sol2))]))
    print("\ntime:", end = ' ')
    print(time.time()-begin)

    print("\n============================================\ntabou\n=========================================\n")
    begin = time.time()
    sol3,decomp3 = tabou.run(N,B,E,quantities,sol,decomp)
    printsol(sol3,decomp3)
    #print("COST", sum([sol3[i][0] for i in range(len(sol3))]))
    print("\ntime:", end = ' ')
    print(time.time()-begin)

    #To comment
    print(sum(quantities) == sum([sum([x for x in j]) for j in sol]))






