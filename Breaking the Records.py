def breakingRecords(scores):
    cmax=cmin=0
    max = min = scores[0]
    for i in scores:
        if i>max :
            max=i
            cmax +=1
        elif i<min :
            min=i
            cmin +=1
    return(cmax,cmin)

if __name__ == '__main__':
   
    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    print(result)
