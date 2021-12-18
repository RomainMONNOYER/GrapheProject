from functions.lecture import *
from functions.printSol import *
from src.functions.Base.BoxFiting import *
from functions.Splitter.smartIncreasing import *
from functions.Metaheuristics.localSearch import *

if __name__ == '__main__':
    N,B,E,quantities = readData("datas/data10.dat")
    sol,decomp = base(N,B,E,quantities)

    printsol(sol,decomp)

    sol,decomp = run(N,B,E,quantities,sol,decomp)
    printsol(sol,decomp)

    #To comment
    print(sum(quantities) == sum([sum([x for x in j]) for j in sol]))






