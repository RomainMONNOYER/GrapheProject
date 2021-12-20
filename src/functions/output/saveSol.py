printdecomp = True


def printsol(sol,decomp,fileDest='temp.txt'):
    with open("functions/output/"+fileDest, 'w') as f:

        #Print decomposition
        if printdecomp:
            i = 1
            for num in decomp:
                f.write(str(i) +" "+ str(num[0]) +" "+ str(len(num[1]))+" ")
                [f.write(str(num) + " ") for num in num[1]]
                f.write("\n")
                i += 1

        #Print Max value for each box
        for i in range(len(sol)):
            f.write("B" + str(i+1) + " " + str(max(sol[i])))
            f.write("\n")

        #Print value
        f.write("COST "+ str(sum([sol[i][0] for i in range(len(sol))])))
        f.write("\n")

        f.close()