cube = lambda x: x**3

def fibonacci(n):
    a=0
    b=1
    l=[]
    for i in range(n):
        l.append(a)
        c=a+b
        a=b
        b=c
    return (l)

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
