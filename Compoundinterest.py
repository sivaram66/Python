PR = float(input("enter the Principal amount"))
rate =float(input('Enter the Rate'))
num= float(input('Number of times interest is compounded per year'))
time=float(input('no of years'))

Amount = PR*(1+rate/num)**(num*time)
print(Amount)
CI = Amount - PR
print(CI)
