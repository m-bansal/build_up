def pageCount(n, p):
    even=0
    if(n%2==0):
        even=1    
    if(p==1 or p==n):
        return('0')
    elif((p-1) < (n-p)):
        return(p//2)
    else:
        if (even==0):
            return((n-p)//2)
        else:
            if((n-p)%2 == 0):
                return((n-p)//2)
            else:
                return(((n-p)//2)+1)
if __name__ == '__main__':
    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    print(result)
