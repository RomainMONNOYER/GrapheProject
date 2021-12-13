from functions.lecture import *
from functions.printSol import *
from src.functions.Solve.temp import *

if __name__ == '__main__':
    N,B,E,quantities = readData("datas/data1.dat")
    BaseSol,decomp = base(N,B,E,quantities)

    # print("\nRun : ")
    # sol = recursive_greedy(B,E,quantities,BaseSol,val,rest)
    printsol(BaseSol,decomp)

    #To comment
    print(sum(quantities) == sum([sum([x for x in j]) for j in BaseSol]))






