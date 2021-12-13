import math

def base(N,B,E,quantities):
    temp = [(x,x) for x in quantities]
    decomp = {}
    for num in quantities:
        decomp[num] = 1

    while len(temp) < B * E:
        temp = []
        for k,v in decomp.items():
            time = k % v
            for i in range(time):
                temp.append((math.ceil(k/v),k))
            for i in range(v-time):
                temp.append((int(k/v),k))
        temp.sort(reverse=True)

        decomp[temp[0][1]] += 1

    sol = []
    for i in range(B):
        sol.append([x[0] for x in temp[i*E:(i+1)*E]])

    for num in quantities:
        decomp[num] = [x[0] for x in temp if x[1] == num]

    return sol,decomp

