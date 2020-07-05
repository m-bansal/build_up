n=int(input("enter a number"))
k=0
for i in range(2,n//2):
    if n%i == 0:
        k=1
if n == 1:
    print('1 is neither prime nor composite')
else:
    if k == 0:
        print('prime')
    else:
        print('not prime')
