import numpy

def arrays(arr):
    n=numpy.array(arr,float)
    return(n[::-1])

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
