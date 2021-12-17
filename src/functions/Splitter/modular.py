import math

def evaluate(N, B, E, quantities, bases,depth):
    # Limit search space
    if bases != sorted(bases):
        return False,False

    temp = [(quantities[i], i) for i in range(len(quantities))]
    sol = []
    decomp = [(num, []) for num in quantities]

    for i in range(depth):  # For each boxes
        base = bases[i]
        currentbox = []
        for j in range(E):
            k = 0
            for l in range(len(temp)):  # If any number is a multiple of base, focus it
                if temp[l][0] % base == 0 and temp[l][0] != 0:
                    k = l

            if temp[k][0] >= base:  # We take base from max number to complete the box
                currentbox.append(base)
                decomp[temp[k][1]][1].append(base)
                temp[k] = (temp[k][0] - base, temp[k][1])
            elif temp[k][0] != 0:  # or the number if it's smaller than the base
                currentbox.append(temp[k][0])
                decomp[temp[k][1]][1].append(temp[k][0])
                temp[k] = (0, temp[k][1])

            temp.sort(key=lambda x: x[0], reverse=True)

        # If box is not full, fill it with 0
        if len(currentbox) < E:
            currentbox += [0] * (E - len(currentbox))

        sol.append(currentbox)

    occupation = math.ceil(N / E)  # Calculate the place the rests will take

    for i in range(len(bases) - depth - occupation):
        base = math.ceil(temp[0][0] / 2)
        brood = base
        fitting = sum([x[0] // base for x in temp])

        # Searching the base that perfectly fill a box (dicotomic search)
        while fitting != E:
            if fitting < E:
                brood = brood // 2
                base -= brood
            else:
                brood = math.ceil(brood / 2)
                base += brood

            fitting = sum([x[0] // base for x in temp])

        # Fill the box
        sol.append([base] * E)
        # Update the number available
        for num in temp:
            decomp[num[1]][1].extend([base] * (num[0] // base))

        temp = sorted([(x[0] % base, x[1]) for x in temp], key=lambda x: x[0], reverse=True)

        # Append rest to decomposition
    for num in temp:
        decomp[num[1]][1].append(num[0])

        # Fulfilling rest with 0 for each missing place
    temp = [x[0] for x in temp] + [0] * (N % E)
    for i in range(occupation):
        sol.append(temp[E * i:E * (i + 1)])

    print(sol)

    # If solution is acceptable, return it
    if sum([len(x) for x in sol]) == B * E:
        return sol, decomp
    else:
        return False, False