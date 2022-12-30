year = eval(input("Enter the Year"))
if (year%4==0) and (year%400==0):
    print("{} is a Leap Year".format(year))
elif (year%100!=0):
    print("{} is a leap year".format(year))
else:
    print("{} is a not a leap year".format(year))
    

