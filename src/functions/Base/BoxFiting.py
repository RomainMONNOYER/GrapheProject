import math

# For each boxes, find a base number to decompose list with.
# N/E rounded up last boxes, each contains the same number (base)
def base(N, B, E, quantities):
    temp = [(quantities[i],i) for i in range(N)]
    sol = []
    decomp = [(num,[]) for num in quantities]

    occupation = math.ceil(N/E) #Calculate the place the rests will take

    # For each boxes that are free (with no rest)
    for i in range(B-occupation):
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

        temp = sorted([(x[0] % base,x[1]) for x in temp],key=lambda x : x[0],reverse=True)

    # Append rest to decomposition
    for num in temp:
        decomp[num[1]][1].append(num[0])

    # Fulfilling rest with 0 for each missing place
    temp = [x[0] for x in temp] + [0] * (N % E)
    for i in range(occupation):
        sol.append(temp[E*i:E*(i+1)])

    return sol,decomp