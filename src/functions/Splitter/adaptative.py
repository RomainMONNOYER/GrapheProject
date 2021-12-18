import math


def evaluate(N, B, E, quantities, bases,depth):
    # Limit search space
    if bases != sorted(bases, reverse=True):
        return False, False

    rest = [(quantities[i], i) for i in range(len(quantities))]
    sol = []
    decomp = [(num, []) for num in quantities]

    boxfilled = 0

    while boxfilled < B - math.ceil(len(rest)/E): # While there's enought boxes to decompose belong a base
        base = bases[boxfilled]
        currentbox = []
        for j in range(E):
            rest = sorted([x for x in rest if x[0] != 0],reverse=True)
            temp = [x for x in rest if x[0] >= base]
            k = 0
            for l in range(len(temp)):  # If any number is a multiple of base, focus it
                if temp[l][0] % base == 0 and temp[l][0] != 0:
                    k = l

            if temp: # We take base from max number to complete the box
                currentbox.append(base)

                # Search temp[k] in rest
                id = temp[k][1]
                pos = 0
                while rest[pos][1] != id:
                    pos += 1

                decomp[rest[pos][1]][1].append(base)
                rest[k] = (rest[pos][0] - base, rest[k][1])
            else :   # or the number if it's smaller than the base
                temp = sorted([x for x in rest if x[0] != 0],reverse=True)

                if temp:
                    currentbox.append(temp[k][0])

                    # Search temp[k] in rest
                    id = temp[k][1]
                    pos = 0
                    while rest[pos][1] != id:
                        pos += 1

                    decomp[rest[pos][1]][1].append(rest[pos][0])
                    rest[pos] = (0, rest[pos][1])
                else:
                    currentbox.append(0)

        rest = sorted([x for x in rest if x[0] != 0], reverse=True)
        sol.append(currentbox)
        boxfilled += 1

    if len(rest) < E * math.ceil(len(rest)/E):
        n = E * math.ceil(len(rest)/E) - len(rest)
        base = rest[n][0]
        for i in range(n):
            rest[i] = (rest[i][0] - base,rest[i][1])
            rest.append((base,rest[i][1]))

        for num in rest:
            decomp[num[1]][1].append(num[0])

        for i in range(math.ceil(len(rest)/E)):
            sol.append([x[0] for x in rest[E*i : E*(i+1)]])

    else:
        sol.append([x[0] for x in rest])
        for num in rest:
            decomp[num[1]][1].append(num[0])

    # If solution is acceptable, return it
    if sum([len(x) for x in sol]) == B * E:
        return sol, decomp
    else:
        return False, False