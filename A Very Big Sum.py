def aVeryBigSum(ar):
    a=0
    for i in range(len(ar)):
        a+=ar[i]
    return a
if __name__ == '__main__':
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = aVeryBigSum(ar)
    print(result)
