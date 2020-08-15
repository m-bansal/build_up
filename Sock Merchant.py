def sockMerchant(n, ar):
    ans=0
    c=[]
    s=set(ar)
    l=list(s)
    for i in l:
        c.append(ar.count(i))
    for j in c:
        ans += (j//2)
    return ans

if __name__ == '__main__':
    
    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(result)
