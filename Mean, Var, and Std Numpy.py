import numpy as np
l=[]
n,m = input().split()
for i in range(int(n)):
    l.append(list(map(int, input().split())))
a = np.array(l)

print(np.mean(a,axis = 1))
print(np.var(a,axis = 0))
print(np.std(a))
