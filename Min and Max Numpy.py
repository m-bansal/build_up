import numpy as np
l=[]
n, m = input().split()

for i in range(int(n)):
    l.append(list(map(int, input().split())))
a = np.array(l)
m=np.min(a, axis = 1)
print(np.max(m))
