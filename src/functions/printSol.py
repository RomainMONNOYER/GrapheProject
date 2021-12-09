
def printsol(sol,decomp):
    #Print decomposition
    i = 1
    for k,v in decomp.items():
        print(i,k,len(v)," ".join(map(str,v)))
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

