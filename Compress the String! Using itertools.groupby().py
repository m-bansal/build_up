import itertools
b=input()
print(*[(len(list(c)),int(k)) for k,c in itertools.groupby(b)])
