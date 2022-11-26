import math as m

#The General Quadraric Equation = a^2 + bx + c = 0



a, b,c = eval(input("enter the Coeffients"))
#find the  discriminant
d = (b**2 - 4*a*c)
if d>0:
    x1 = (-b+m.sqrt(d))/(2*a)
    x2 = (-b-m.sqrt(d))/(2*a)
    print("solution: {},{}".format(x1,x2))
else:
    print("no solution")
