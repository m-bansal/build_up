def merge_the_tools(s, k):
    seg=int(len(s)/k)
    for i in range(seg):
        t=s[i*k : (i+1)*k]
        u=""
        for m in t:
            if m not in u:
                u+=m
        print(u)
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
