def pickingNumbers(a):
    max=0
    for i in a:
        c=a.count(i)
        d=a.count(i-1)
        c+=d
        if c>max:
            max=c
    return max

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    print(result)
