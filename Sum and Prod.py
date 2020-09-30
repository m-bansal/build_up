import numpy as np
n, m = input().split()
l=[]
for i in range(int(n)):
    l.append(list(map(int, input().split())))
a = np.array(l)
sum_axis0 = np.sum(a,axis = 0)
print(np.prod(sum_axis0))
