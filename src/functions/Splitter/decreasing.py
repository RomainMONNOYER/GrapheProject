def evaluate(N,B,E,quantities,bases):
    temp = [(quantities[i], i) for i in range(len(quantities))]
    sol = []
    decomp = [(num, []) for num in quantities]

    for i in range(len(bases)): # For each boxes
        base = bases[i]
        currentbox = []
        for j in range(E):  # We take base from max number to complete the box
            if temp[0][0] >= base:
                currentbox.append(base)
                decomp[temp[0][1]][1].append(base)
                temp[0] = (temp[0][0] - base,temp[0][1])
            elif temp[0][0] != 0:   # or the number if it's smaller than the base
                currentbox.append(temp[0][0])
                decomp[temp[0][1]][1].append(temp[0][0])
                temp[0] = (0, temp[0][1])

            temp.sort(key=lambda x: x[0], reverse=True)

        sol.append(currentbox)

    # If any rest remain, add to sol for analysing
    rest = [x[0] for x in temp if x[0] != 0]
    if rest:
        sol.append(rest)

    # If solution is acceptable, return it
    if sum([len(x) for x in sol]) == B * E:
        return sol,decomp
    else:
        return False,False