import math

# From starting number, split max element in 2 to complete the box.
# If number has already been cut, restart from original and cut it in 3,4,5,...
def base(N,B,E,quantities):
    temp = [(quantities[i],i) for i in range(N)]
    decomp = {}
    for i in range(N):
        decomp[i] = 1

    # While box is not full ...
    while len(temp) < B * E:
        temp = []
        # For each number ...
        for i,v in decomp.items():
            time = quantities[i] % v # Evaluate the number of part to make
            for j in range(time):
                temp.append((math.ceil(quantities[i]/v),i))
            for j in range(v-time):
                temp.append((int(quantities[i]/v),i))
        temp.sort(key=lambda x: x[0],reverse=True)

        decomp[temp[0][1]] += 1

    sol = []
    decomp = []

    # Separate list in each box of lenght E
    for i in range(B):
        sol.append([x[0] for x in temp[i*E:(i+1)*E]])

    # Evaluate score
    for num in quantities:
        decomp.append((num,[x[0] for x in temp if quantities[x[1]] == num]))

    return sol,decomp

