import numpy as np
n,m,p = map(int, input().split())
a1=np.array([input().split() for i in range(n)],int)
a2=np.array([input().split() for i in range(m)],int)
print(np.concatenate((a1, a2), axis=0))
