def kangaroo(x1, v1, x2, v2):
    for i in range(1,10001):
        if((x1+(v1*i))==(x2+(v2*i))):
            return('YES')
    return('NO')
if __name__ == '__main__':
    x1V1X2V2 = input().split()
    
    x1 = int(x1V1X2V2[0])
    v1 = int(x1V1X2V2[1])
    x2 = int(x1V1X2V2[2])
    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    print(result)
