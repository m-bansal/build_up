def catAndMouse(x, y, z):
    a1=abs(z-x)
    a2=abs(z-y)
    if(a1<a2):
        return("Cat A")
    elif(a1>a2):
        return("Cat B")
    else:
        return("Mouse C")


if __name__ == '__main__':
    
    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        print(result)
