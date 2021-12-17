base = [x for x in [1,2,3,4,8]]
value = sum(base)
step = 1
V = [True]


for i in range(len(base)):
    tempbase = [x for x in base]
    tempbase[i] -= step
    print(tempbase)

print(base)