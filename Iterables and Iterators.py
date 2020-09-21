import itertools
n=int(input())
count=0
l=input().split()
k=int(input())
c=list(itertools.combinations(l,k))
for i in c:
    if 'a' in i:
        count+=1
print(round((count/(len(c))),3))
