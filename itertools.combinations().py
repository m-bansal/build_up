from itertools import combinations
s,k=input().split()
for i in range(1,int(k)+1):
    l=combinations(sorted(s),i)
    for i in l:
        print(''.join(i))
