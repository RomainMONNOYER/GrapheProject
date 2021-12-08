
def printsol(sol):
    print("\nSolution :\n")
    for i in range(len(sol)):
        print(sol[i])

    print("\n\nValue :",sum([sol[i][0] for i in range(len(sol))]))