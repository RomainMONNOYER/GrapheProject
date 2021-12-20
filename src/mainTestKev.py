from functions.lecture import *
from functions.output.saveSol import *

import PotionSAR_SAP_LS as potion

if __name__ == '__main__':
    #best = [5243,8190,3897,9978,4966,15030,7194,239778,229428,226788]

    N,B,E,quantities = readData("datas/data10.dat")
    sol,decomp,timeTaken = potion.runPotion(N,B,E,quantities)

    printsol(sol,decomp,fileDest = "temp.txt")
    print(round(timeTaken,3))
