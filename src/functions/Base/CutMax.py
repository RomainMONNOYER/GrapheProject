import math

# From starting number, split max element in 2 to complete the box
def base(N,B,E,quantities):
    sol = []
    decomp = []
    temp = [(x,x) for x in quantities]

    # While box is not full ...
    while len(temp) < B * E:
        num = temp[0][0] # Take max
        temp[0] = (math.ceil(num/2),temp[0][1]) # Cut it in half
        temp.append((num - temp[0][0],temp[0][1])) # Append second half to end

        temp.sort(key =  lambda tup:tup[0], reverse = True) # Sort

    # Separate list in each box of lenght E
    for i in range(B):
        sol.append([x[0] for x in temp[i*E:(i+1)*E]])

    # Evaluate score
    for num in quantities:
        decomp.append((num,[x[0] for x in temp if x[1] == num]))

    return sol,decomp


