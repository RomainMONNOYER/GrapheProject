import math

def base(N,B,E,quantities):
    sol = []
    base = math.ceil(sol[0]/2)

    val = [x // base for x in quantities]
    rest = [x % base for x in quantities]

    pack = sum(val) + sum([x for x in rest if x != 0])
    
    

