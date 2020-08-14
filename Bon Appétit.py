def bonAppetit(bill, k, b):
    sum=0
    for i in range(len(bill)):
        if(i != k):
            sum+=bill[i]
        else:
            continue
    act=sum//2
    if(act == b):
        print('Bon Appetit')
    else:
        print(b-act)

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
