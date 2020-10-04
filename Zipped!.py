n, x = map(int, input().split())
l=[]
for i in range(x):
    l.append(list(map(float, input().split())))
for i in zip(*l):
    print(sum(i)/x)
