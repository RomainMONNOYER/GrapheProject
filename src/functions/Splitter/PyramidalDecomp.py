import math

def evaluate(quantities,bases):
    temp = [(quantities[i], i) for i in range(len(quantities))]
    sol = []
    decomp = [(num, []) for num in quantities]

    for i in range(len(bases)):
        base = bases[i]

        for num in temp:
            decomp[num[1]][1].extend([base] * (num[0] // base))

        temp = sorted([(x[0] % base,x[1]) for x in temp],key=lambda x : x[0],reverse=True)