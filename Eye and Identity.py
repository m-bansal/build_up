import numpy as np
rows, cols = map(int, input().split())
print (str(np.eye(rows, cols, k = 0)).replace('1', ' 1').replace('0', ' 0'))
