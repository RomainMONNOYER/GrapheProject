from functions.lecture import *
from functions.Base.BoxFiting import *
from functions.Splitter.smartIncreasing import *
from functions.Metaheuristics.recuitGlobal import *
from functions.printSol import *

if __name__ == '__main__':
    N,B,E,quantities = readData("datas/data1.dat")
    sol,decomp = base(N,B,E,quantities)
    printsol(sol, decomp)

    sol,decomp = run(N,B,E,quantities,sol,decomp)
    printsol(sol,decomp)

    # To comment
    if sum(quantities) == sum([sum(x) for x in sol]):
        print("Solution is ok")
    else:
        print("Problem ! Sum of value not equal")