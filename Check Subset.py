n=int(input())
for i in range(n):
    a_no = int(input())
    a = list(set(map(int, input().split())))
    b_no = int(input())
    b = list(set(map(int, input().split())))
    for i in a:
        if i in b:
            if i==a[a_no-1]:
                print("True")
            continue
        else:
            print("False")
            break
