def evaluate(N, B, E, quantities, bases,depth):
    # Limit search space
    if bases != sorted(bases, reverse=True):
        return False, False

    temp = [(quantities[i], i) for i in range(len(quantities))]
    sol = []
    decomp = [(num, []) for num in quantities]

    for i in range(len(bases)): # For each boxes
        base = bases[i]
        currentbox = []
        for j in range(E):
            k = 0
            for l in range(len(temp)):  # If any number is a multiple of base, focus it
                if temp[l][0] % base == 0 and temp[l][0] != 0:
                    k = l

            if temp[k][0] >= base: # We take base from max number to complete the box
                currentbox.append(base)
                decomp[temp[k][1]][1].append(base)
                temp[k] = (temp[k][0] - base, temp[k][1])
            elif temp[k][0] != 0:   # or the number if it's smaller than the base
                currentbox.append(temp[k][0])
                decomp[temp[k][1]][1].append(temp[k][0])
                temp[k] = (0, temp[k][1])

            temp.sort(key=lambda x: x[0], reverse=True)

        # If box is not full, fill it with 0
        if len(currentbox) < E:
            currentbox += [0] * (E - len(currentbox))

        sol.append(currentbox)

    # If any rest remain, add to sol for analysing
    rest = [x[0] for x in temp if x[0] != 0]
    if rest:
        sol.append(rest)

    # If solution is acceptable, return it
    if sum([len(x) for x in sol]) == B * E:
        return sol, decomp
    else:
        return False, False