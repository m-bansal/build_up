def miniMaxSum(arr):
    mx=max(arr)
    mn=min(arr)
    sm=sum(arr)
    print(sm-mx,sm-mn)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
