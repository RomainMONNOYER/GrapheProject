printdecomp = True


def printsol(sol,decomp):
    #Print decomposition
    if printdecomp:
        i = 1
        for num in decomp:
            print(i,num[0],len(num[1])," ".join(map(str,num[1])))
            i += 1

    #Print Max value for each box
    for i in range(len(sol)):
        print("B{}".format(i+1),max(sol[i]))

    #Print value
    print("COST", sum([sol[i][0] for i in range(len(sol))]))

    #To comment at the end
    print("\nSolution :")
    for i in range(len(sol)):
        print(sol[i])

