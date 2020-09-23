from collections import deque
d = deque()
n=int(input())
for i in range(n):
    a=input().split()
    cmd=a[0]
    if cmd=='append':
        d.append(a[1])
    elif cmd=='pop':
        d.pop()
    elif cmd=='popleft':
        d.popleft()
    elif cmd=='appendleft':
        d.appendleft(a[1])
print(*d)
