from collections import namedtuple
tot_stu = int(input())
a=0
fields = input().split()

for i in range(tot_stu):
    stu = namedtuple('stu',fields)
    field1, field2, field3,field4 = input().split()
    stu= stu(field1,field2,field3,field4)
    a+=int(stu.MARKS)
print('{:.2f}'.format(a/tot_stu))
