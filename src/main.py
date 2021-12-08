from functions.lecture import *
from functions.printSol import *
from src.functions.Base.BaseSol_ModularDecomposition import *
from functions.Solve.Recursive_Greedy import *

if __name__ == '__main__':
    N, E, B, quantities = readData("datas/data1.dat")
    print("N,E,B,quantities : ",N, E, B, quantities)

    BaseSol,val,rest = base(B,E,quantities)

    # print("\nRun : ")
    # sol = recursive_greedy(B,E,quantities,BaseSol,val,rest)
    #
    # printsol(sol)
    #
    # print("\n\nVerif :")
    # print("Init : ", sum(quantities))
    # print("Sol : ", sum([sum([x for x in j]) for j in sol]),"\n")







