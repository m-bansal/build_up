def countingValleys(n, s):
    l=0
    lst=[]
    c=0
    for i in s:
        if i=='D':
            l-=1
            lst.append(l)
        elif i=='U':
            l+=1
            lst.append(l)
        if l==0:
            see=lst[-2]
            if (see < 0):
                c+=1
    return c

if __name__ == '__main__':
    n = int(input())

    s = input()

    result = countingValleys(n, s)

    print(result)
