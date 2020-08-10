def birthday(s, d, m):    
    c=0
    for i in range(n-m+1):
        l=0
        for j in range(i,i+m):
            l+=s[j]
        if l==d :
            c+=1
    return c

if __name__ == '__main__':
    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    print(result)
