def readData(inputFileName):
    with open(inputFileName) as f:
        lines = [int(line) for line in f.readlines()]
        N, E, B = lines[:3]                                 #3 First lines of the file are N, E, B
        quantities = sorted(lines[3:], reverse = True)        #Others N lines are the quantity. Nothings says it's already sorted.
    return N, E, B, quantities