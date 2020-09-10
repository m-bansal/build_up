A_no=int(input())
A = set(map(int, input().split()))
N = int(input())
for i in range(N):
    opr, no = input().split()
    s = set(map(int, input().split()))

    if opr == 'intersection_update':
        A &= s
    elif opr == 'update':
        A |= s
    elif opr == 'symmetric_difference_update':
        A ^= s
    else:
        A -= s
print(sum(A))
