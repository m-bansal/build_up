n = int(input())
arr = list(input().split())
x=max(arr)
y=arr.count(x)
for i in range(y):
    arr.remove(x)
z=max(arr)
print(z)
