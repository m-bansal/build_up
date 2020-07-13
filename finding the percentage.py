def avg(list):
    print('{:.2f}'.format((list[0]+list[1]+list[2])/3))
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    avg(student_marks[query_name])
