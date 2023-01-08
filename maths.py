print("1 = Triangle")
print("2 = Square")
print("3 = rectangle")
print("4 = circle")
print("5 = semi circle")
print("6 = cylinder")
print("7 = cone")
print("8 = cube")
print("9 = cuboid")
print("10= right angle triange")
print("chr= characters")
a=(int(input("enter value")))
import math
if(a==1):
    print("triangle")
    a=int(input("enter first side= "))
    b=int(input("enter first side= "))
    c=int(input("enter first side= "))
    if(a==b and c==a):
        print("equilateral")
        print("perimeter =", a+b+c)
        print("area =",math.sqrt(((a+b+c)/2)+((a+b+c)-a)+((a+b+c)-b)+((a+b+c)-c)))
    elif(a==b or b==c or c==a):
        print("isosceles")    
    else:
        print("scalene")
elif(a==2):
    print("square")
    a=int(input("enter side= "))
    print("perimeter = ", a*4)
    print("area = ",a*a)
    
elif(a==3):
    l=int(input("enter length= "))
    b=int(input("enter breadth= "))
    print("perimeter of rectangle:",2(l+b))
    print("perimeter of rectangle:",l*b)
elif(a==4):
    r=int(input("enter radius= "))
    print("circumference of circle:",2*22/7*r)
    print("area of circle:",22/7*r*r)
elif(a==5):
    r=int(input("enter radius= "))
    print("circumference of semi-circle:",(2*22/7*r)/2)
    print("area of circle:",(22/7*r*r)/2)
elif(a==6):
    r=int(input("enter radius= "))
    h=int(input("enter height= "))
    print("T.S.A of cyclinder:",(2*22/7*r*h)+(2*22/7*r))
    print("volume of cylinder:",22/7*r*r*h)
elif(a==7):
    r=int(input("enter radius= "))
    l=int(input("enter slant-height= "))
    print("T.S.A of cone:",(22/7*r*(r+l)))
    print("L.S.A of cone:",22/7*r*l)
elif(a==8):
    a=int(input("enter side of cube= "))
    print("T.S.A Of cube:",6*a*a)
    print("volume of cube:",a*a*a)
elif(a==9):
    l=int(input("enter length of cuboid= "))
    b=int(input("enter breadth of cuboid= "))
    h=int(input("enter height of cuboid= "))
    print("T.S.A Of cube:",2(l*b+b*h+h*l))
    print("volume of cube:",l*b*h)
elif(a==chr):
    a=str(input(a >= 'a' and a <= 'z') or (a >= 'A' and a <= 'Z'))
    print("alphabet")
elif(a==10):
    print("right angle triangle")
    for i in range(1,11,1):
        for j in range(1,i,1):
            print(":)",end='')
        print()
else:
    print("it is a special character")
