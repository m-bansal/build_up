def hurdleRace(k, height):
    if max(height)<=k:
        return 0
    else:
        return(max(height)-k)

if __name__ == '__main__':    

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    height = list(map(int, input().rstrip().split()))

    result = hurdleRace(k, height)

    print(result)
