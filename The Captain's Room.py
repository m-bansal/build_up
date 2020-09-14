k=int(input())
room = list(map(int, input().split()))
room.sort()
i=0
while(i<len(room)):
    if (i == len(room)-1):
        print(room[i])
        break
    if room[i]!=room[k+i-1]:
        print(room[i])
        break
    i+=k
