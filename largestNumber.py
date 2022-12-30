Num1 = eval(input("Enter the 1st Number"))
Num2 = eval(input("Enter the 2nd Number"))
Num3 = eval(input("Enter the 3nd Number"))
if (Num1 >Num2) and (Num1 >Num3):
    print("{} is the Largest Number".format(Num1))
if (Num2 >Num1) and (Num2 > Num3):
    print("{} is the Largest Number".format(Num2))
if(Num3 >Num1) and  (Num3 >Num2):
    print("{} is the Largest Number".format(Num3))
