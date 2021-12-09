import math

def base(B, E, quantities):
    sol = quantities
    decomp = {}
    for num in quantities:
        decomp[num] = 1

    # Split max element in 2
    while len(sol) < B * E:
        sol = []
        for k,v in decomp:
            for i in range(v):
                sol.append()

        num = temp[0][0]
        temp[0] = (math.ceil(num/2),temp[0][1])
        temp.append((num - temp[0][0],temp[0][1]))

        temp.sort(key =  lambda tup:tup[0], reverse = True)

    for i in range(B):
        sol.append([x[0] for x in temp[i*E:(i+1)*E]])

    for num in quantities:
        decomp[num] = [x[0] for x in temp if x[1] == num]

    return sol,decomp