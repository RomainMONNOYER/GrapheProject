import math
import time

def recursive_greedy(B,E,quantities,baseSol,val,rest):
    sol = baseSol
    prevbase = quantities[-1]
    objective = sum([sum([x for x in j]) for j in sol])
    prevobjective = objective
    while objective <= prevobjective:
        base = max(rest)
        if base < prevbase/2:
            return sol

        tempsol = []
        val = [x // base for x in quantities]
        rest = [x % base for x in quantities]
        pack = sum(val)

        # Box 1 with maximum value (multiple of base)
        v1 = math.ceil((pack - (B - 2) * E) / E) * base
        r1 = (pack - (B - 2) * E) % E
        temp = []
        for i in range(r1):
            temp.append(v1)
        for i in range(E - r1):
            temp.append(v1 - base)
        tempsol.append(temp)

        # Bax 2 .. B-1 of base
        for i in range(B - 2):
            temp = []
            for j in range(E):
                temp.append(base)
            tempsol.append(temp)

        # Box B with rest
        tempsol.append(sorted(rest,reverse=True))

        prevbase = base
        prevobjective = objective
        objective = sum([tempsol[i][0] for i in range(B)])
        if objective <= prevobjective:
            sol = tempsol
        print("Value :",objective," Base :",base)

        time.sleep(1)


    return sol