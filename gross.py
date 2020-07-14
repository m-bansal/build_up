h=float(input("Enter hours"))
r=float(input("Enter rate per hour"))
n=input("Enter name")
pay=0
if h<=37.5 :
    pay=r*h
elif h>37.5 :
    pay=(r*37.5) + ((h-37.5)*1.5*r)
print(n,"your gross pay is",pay,"CAD")
