import math

def base(N, B, E, quantities):
    temp = quantities
    sol = []
    decomp = {num : 1 for num in quantities}

    for i in range(B-1):
        base = math.ceil(temp[0] / 2)
        brood = base
        fitting = sum([x // base for x in temp])

        while fitting != E:
            if fitting < E:
                brood = brood // 2
                base -= brood
            else:
                brood = math.ceil(brood / 2)
                base += brood

            fitting = sum([x // base for x in temp])

        sol.append([base] * E)
        temp = sorted([x % base for x in temp],reverse=True)

    sol.append(temp)

    return sol,decomp

