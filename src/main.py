from functions.lecture import *
from functions.printSol import *
from src.functions.Solve.BoxFiting import *

if __name__ == '__main__':
    N,B,E,quantities = readData("datas/data1.dat")
    BaseSol,decomp = base(N,B,E,quantities)

    printsol(BaseSol,decomp)

    #To comment
    print(sum(quantities) == sum([sum([x for x in j]) for j in BaseSol]))






