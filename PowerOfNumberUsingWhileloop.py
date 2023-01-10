Num =eval(input("Enter the number:"))
result= list(map(lambda x :Num**x,range(0,11)))
for i in range(0,11):
    print(Num,'Raised to',i,'=',result[i])