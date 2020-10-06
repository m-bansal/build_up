if __name__ == '__main__':
    n,m = map(int, input().split())
    
    l = [list(map(int, input().rstrip().split())) for _ in range(n)]
    k = int(input())

    l.sort(key=lambda x: x[k])

    for i in l:
        print(*i)
