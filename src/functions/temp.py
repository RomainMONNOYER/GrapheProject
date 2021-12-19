import itertools
lst = list(itertools.product([0, 1], repeat=5))

print([list(x) for x in lst[1:]])