from collections import deque
t=int(input())
working_cube = -1
for i in range(t):
    int(input())
    l=deque(map(int, input().split()))
    while l:
        working_cube = l.popleft() if l[0]>l[-1] else l.pop()
        if not l:
            print("Yes")
            break
        if l[-1]>working_cube or l[0]>working_cube:
            print("No")
            break
