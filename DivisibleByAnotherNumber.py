

##using for for loop 
Start = eval(input("Enter the Starting Number:"))
End =eval(input('Enter the Last Number:'))
Divisor = eval(input("Enter the Divisor:"))
for i in range(Start,End+1):
    if i %Divisor==0:
        print(i)
