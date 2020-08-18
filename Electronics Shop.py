def getMoneySpent(keyboards, drives, b):
    l=[]
    if(min(keyboards) + min(drives)) > b :
        return('-1')
    else:
        for i in keyboards:
            for j in drives:
                if((i+j)>b):
                    continue
                l.append(i+j)
        l.sort()
        return(l[-1])

if __name__ == '__main__':
    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    moneySpent = getMoneySpent(keyboards, drives, b)

    print(moneySpent)
