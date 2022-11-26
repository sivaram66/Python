Pr = float(input("enter the Principal amount"))
rate =float(input('Enter the Rate'))
num= int(input('Number of times interest is compounded per year'))
time=float(input('no of years'))

Amount = Pr*(1+rate/num)**(num*time)
print(Amount)
CI = Amount - Pr
print(CI)
