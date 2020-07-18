from itertools import permutations
word,no=input().split()
l=tuple(permutations(word,int(no)))
m=sorted(l)
for i in range(len(m)):
    print(''.join(m[i]))
