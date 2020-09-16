a = set(map(int, input().split()))
n=int(input())
ans=True
for i in range(n):
    s = set(map(int, input().split()))
    diff = s.difference(a)
    if(len(diff)==0 and len(a.difference(s))>=1):
        continue
    else:
        ans=False
print(ans)
