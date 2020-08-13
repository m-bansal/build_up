def dayOfProgrammer(year):
    jan_aug=215
    if(year<1918):
        if(year%4 == 0):
            feb=29        
        else:
            feb=28        
    
    if(year>1918):
        if(year%400 == 0):
            feb=29
        elif (year%4 ==0 and year%100 != 0):
            feb=29
        else:
            feb=28

    if(year == 1918):
        feb=15

    date = 256 - (feb + jan_aug)
    return(str(date) + ".09." + str(year))

if __name__ == '__main__':

    year = int(input().strip())

    result = dayOfProgrammer(year)

    print(result)
