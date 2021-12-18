def evaluate(N, B, E, quantities, bases,depth):
    # Limit search space
    if bases != sorted(bases, reverse=True):
        return False, False

    rest = [(quantities[i], i) for i in range(len(quantities))]
    sol = []
    decomp = [(num, []) for num in quantities]

    for i in range(len(bases)): # For each boxes
        base = bases[i]
        currentbox = []
        for j in range(E):
            rest = sorted([x for x in rest if x[0] != 0],reverse=True)
            temp = [x for x in rest if x[0] >= base]
            k = -1
            for l in range(len(temp)):  # If any number is a multiple of base, focus it
                if temp[l][0] % base == 0 and temp[l][0] != 0:
                    k = l

            if temp: # We take base from max number to complete the box
                currentbox.append(base)

                # Search temp[k] in rest
                id = temp[k][1]
                pos = 0
                while rest[k][1] != id:
                    pos += 1

                decomp[rest[pos][1]][1].append(base)
                rest[k] = (rest[pos][0] - base, rest[k][1])
            else :   # or the number if it's smaller than the base
                currentbox.append(temp[k][0])

                # Search temp[k] in rest
                id = temp[k][1]
                pos = 0
                while rest[k][1] != id:
                    pos += 1

                decomp[rest[pos][1]][1].append(rest[pos][0])
                rest[pos] = (0, rest[pos][1])

        # If box is not full, fill it with 0
        if len(currentbox) < E:
            currentbox += [0] * (E - len(currentbox))

        sol.append(currentbox)

    # If any rest remain, add to sol for analysing
    rest = [x[0] for x in rest if x[0] != 0]
    if rest:
        sol.append(rest)

    # If solution is acceptable, return it
    if sum([len(x) for x in sol]) == B * E:
        return sol, decomp
    else:
        return False, False