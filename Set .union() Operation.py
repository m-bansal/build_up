e=int(input())
English=set(map(int, input().split()))
f=int(input())
French=set(map(int, input().split()))
print(len(list(English.union(French))))



