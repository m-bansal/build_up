def timeConversion(s):      
    t=s.split(':')
    h=int(t[0])
    m=int(t[1])
    sc=int(t[2][:2])
    ampm=t[2][2:]
    if(ampm=='AM' and h==12):
        h=0
    if(ampm=='PM' and h<12):
        h+=12
    return(('%02d:%02d:%02d') % (h, m, sc))
    
    
if __name__ == '__main__':
    s = input()
    result = timeConversion(s)
    print(result)
