from lecture import *
from src.functions.Solve.SplitMax import *

script = "SplitMax"
out = open("results/" + script + ".txt","w")

if __name__ == '__main__':
    for i in range(1,11):
        N, E, B, quantities = readData("../datas/data{}.dat".format(i))

        BaseSol,decomp = base(B,E,quantities)
        print("COST", sum([BaseSol[i][0] for i in range(len(BaseSol))]))

        out.write("data{} : ".format(i) + str(sum([BaseSol[i][0] for i in range(len(BaseSol))])) + "\n")

out.close()



