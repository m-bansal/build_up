def climbingLeaderboard(scores, alice):
    scores=list(set(scores))
    scores.sort(reverse=True)
    alice.sort(reverse=True)
    l=[]
    j=0
    for i in range(len(alice)):
        while j<len(scores) and alice[i]<scores[j]:
            j+=1
        l.append(j+1)
    return('\n'.join(map(str, l[::-1])))
        
if __name__ == '__main__':

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    print(result)
