from collections import Counter

if __name__ == '__main__':
    s = input()
    c = Counter(sorted(s)).most_common(3)
    for i in c:
        print(*i)
