a=['a','b','c']
b=[1,2,3]

c=list(zip(a,b))
print(c)

d=list(zip(*c))
print(d)

e=dict(zip(a,b))
print(e)
