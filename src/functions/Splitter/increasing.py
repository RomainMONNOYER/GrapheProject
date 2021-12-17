import math

def evaluate(N,B,E,quantities,bases):
    temp = [(quantities[i], i) for i in range(len(quantities))]
    sol = []
    decomp = [(num, []) for num in quantities]

    for i in range(len(bases)):
        base = bases[i]

        currentbox = []
        for j in range(E):
            if temp[0][0] >= base:
                currentbox.append(base)
                decomp[temp[0][1]][1].append(base)
                temp[0] = (temp[0][0] - base,temp[0][1])
            elif temp[0][0] != 0:
                currentbox.append(temp[0][0])
                decomp[temp[0][1]][1].append(temp[0][0])
                temp[0] = (0, temp[0][1])

            temp.sort(key=lambda x: x[0], reverse=True)

        sol.append(currentbox)

    rest = [x[0] for x in temp if x[0] != 0]
    if rest:
        sol.append(rest)


    if sum([len(x) for x in sol]) == B * E:
        return sol,decomp
    else:
        return False,False