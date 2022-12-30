import math as M

#The General Quadratic Equation = a^2 + bx + c = 0

a, b,c = eval(input("Enter the Coeffients"))
#find the  discriminant
d = (b**2 - 4*a*c)
if d>0:
    x1 = (-b+M.sqrt(d))/(2*a)
    x2 = (-b-M.sqrt(d))/(2*a)
    print("solution: {},{}".format(x1,x2))
else:
    print("no solution")
