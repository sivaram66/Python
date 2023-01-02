x = eval(input("Enter The Number "))

if x ==1:
    print(x,"is not a prime number")
elif x >1:
    for i in range(2,x):
        if x%i==0:
            print("{} is Not a Prime Number".format(x))
            break
    else:
            print("{} is a prime Number".format(x))
