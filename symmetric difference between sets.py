mn=int(input())
m=set(map(int,input().split()))
nn=int(input())
n=set(map(int,input().split()))
a=m.difference(n)
b=n.difference(m)
c=a.union(b)
l=list(c)
l.sort()
for i in l:
    print(i)
