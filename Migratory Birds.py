def migratoryBirds(arr):
    l=[]
    s=set(arr)
    for i in s:
        l.append(arr.count(i))
    m=max(l)
    for i in s:
        if(arr.count(i) == m):
            return i
if __name__ == '__main__':
    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    print(result)
