from src.functions.lecture import *
from src.functions.Base.BoxFiting import *
from src.functions.Metaheuristics.tabou import *

script = "tabou - adaptative(20,10)"
out = open("results/" + script + ".txt","w")
result = [5243,8190,3897,9978,4966,15030,7194,239778,229428,226788]

if __name__ == '__main__':
    print("--- Evaluating {} ---".format(script))
    for i in range(1,10):
        N,B,E,quantities = readData("../datas/data{}.dat".format(i))

        BaseSol,decomp = base(N,B,E,quantities)

        BaseSol,decomp = run(N,B,E,quantities,BaseSol,decomp)
        cost = sum([BaseSol[i][0] for i in range(len(BaseSol))])
        efficiency = 100*cost/result[i-1] - 100

        print("Data{}  | COST : {}, Efficiency : {} %".format(i,cost,round(efficiency,4)))
        out.write("Data{}  | COST : {}, Efficiency : {} %\n".format(i,cost,round(efficiency,4)))

    N, B, E, quantities = readData("../datas/data10.dat")

    BaseSol, decomp = base(N, B, E, quantities)
    cost = sum([BaseSol[i][0] for i in range(len(BaseSol))])
    efficiency = 100 * cost / result[9] - 100

    print("Data10 | COST : {}, Efficiency : {} %".format(cost, round(efficiency,4)))
    out.write("Data10 | COST : {}, Efficiency : {} %\n".format(cost, round(efficiency,4)))

out.close()



