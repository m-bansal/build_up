#find the intersection of two lists
l=[]
l1=[1,2,3,4]
l2=[2,4,6,7]
def intersect():
    for x in l1:
        if x in l2:
            l.append(x)
    return l
k=intersect()
print(k)
