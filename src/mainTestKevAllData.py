from functions.lecture import *
from functions.printSol import *
from src.functions.Base.BoxFiting import *
from functions.Splitter.smartIncreasing import *

import functions.Metaheuristics.localSearch as localSearch
import functions.Metaheuristics.recuit as recuit
import functions.Metaheuristics.tabou as tabou
import functions.Metaheuristics.SARtabou as SARtabou

import time

import PotionSAR_SAP_LS as potion

if __name__ == '__main__':
    best = [5243,8190,3897,9978,4966,15030,7194,239778,229428,226788]
    data = [{"id":i+1,"cost": 0, "time":0, "best":best[i]} for i in range(10)]

    for d in range(10):
        N,B,E,quantities = readData("datas/data"+str(data[d]["id"])+ ".dat")
        sol,decomp,timeTaken = potion.runPotion(N,B,E,quantities)

        data[d]["cost"] = sum([s[0] for s in sol])
        data[d]["time"] = round(timeTaken, 3)
        data[d]["%"] = round((data[d]["cost"]-data[d]["best"])/data[d]["best"]*100,3)

    [print(d) for d in data]
