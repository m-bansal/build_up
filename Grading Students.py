def gradingStudents(grades):
    l=[]
    for i in grades:
        if i<38 :
            l.append(i)
        else:
            if ((i%5)>=3):
                l.append((5-(i%5))+i)
            else:
                l.append(i)
    return l
'''
        if i<38 or (i%5 < 3):
            l.append(i)
        else:
            l.append((5-(i%5))+i)
'''
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
