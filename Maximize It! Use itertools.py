from itertools import product
ele=[]
k,m = map(int,input().split())
for i in range(k):
    ele.append(list(map(int, input().split()))[1:])
res = map(lambda x : sum(i**2 for i in x) % m, product(*ele))
print(max(res))
