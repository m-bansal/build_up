n = int(input("Enter the no. of times you want to run the loop"))
a=0
b=1
for x in range(0,n):
    print(a)
    c=a+b
    a=b
    b=c
