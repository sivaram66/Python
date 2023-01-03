x = int(input("Enter the Staring Number"))
y = int(input("Enter the Last Number"))

for num in range(x,y):
    if num>1:
        for i in range(2,num):
            if num%i==0:
             break
        else:
            print(num)



