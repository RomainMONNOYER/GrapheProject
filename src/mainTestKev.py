from functions.lecture import *
from functions.output.saveSol import *

import PotionR_SAR_SAP_LS as potion1
import PotionR_SAR_SAP_LSG as potion2
import PotionRG_SAR_SAP_LSG as potion3
import PotionSAR_SAP_LS as potion4
import PotionSAR_SAP_LSG as potion5

import time

if __name__ == '__main__':
    #best = [5243,8190,3897,9978,4966,15030,7194,239778,229428,226788]

    AllSol = []
    begin = time.time()

    N,B,E,quantities = readData("datas/data10.dat")

    #R_SAR_SAP_LS
    sol,decomp,_ = potion1.runPotion(N,B,E,quantities)
    AllSol.append({"sol":sol, "decomp":decomp, "cost":sum([s[0] for s in sol])})

    #R_SAR_SAP_LSG
    #sol,decomp,_ = potion2.runPotion(N,B,E,quantities)
    #AllSol.append({"sol":sol, "decomp":decomp, "cost":sum([s[0] for s in sol])})

    #RG_SAR_SAP_LSG
    #sol,decomp,_ = potion3.runPotion(N,B,E,quantities)
    #AllSol.append({"sol":sol, "decomp":decomp, "cost":sum([s[0] for s in sol])})

    #SAR_SAP_LS
    sol,decomp,_ = potion4.runPotion(N,B,E,quantities)
    AllSol.append({"sol":sol, "decomp":decomp, "cost":sum([s[0] for s in sol])})

    #SAR_SAP_LSG
    #sol,decomp,_ = potion5.runPotion(N,B,E,quantities)
    #AllSol.append({"sol":sol, "decomp":decomp, "cost":sum([s[0] for s in sol])})

    min = 0
    for i in range(len(AllSol)):
        if AllSol[i]["cost"] < AllSol[min]["cost"]:
            min = i

    printsol(AllSol[min]["sol"],AllSol[min]["decomp"],fileDest = "temp.txt")
    print(round(time.time()-begin, 3))



