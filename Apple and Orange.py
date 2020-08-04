def countApplesAndOranges(s, t, a, b, apples, oranges):
    c_a=0;c_b=0
    for i in apples:        
        if (i+a)>=s and (i+a)<=t:
            c_a+=1

    for j in oranges:        
        if (j+b)>=s and (j+b)<=t:
            c_b+=1
    print(c_a)
    print(c_b)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)


