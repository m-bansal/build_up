def getTotalX(a, b):    
    count=0
    for i in range(a[-1],b[0]+1):
        for j in a:
            if(i%j != 0):
                break
            if (j==a[-1]):
                for k in b:
                    if (k%i != 0):
                        break
                    if (k==b[-1]):
                        count+=1                                     
    return count

if __name__ == '__main__':
    
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    print(result)
