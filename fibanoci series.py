a=0
n=int(input("enter the number of terms you want"))
b=1
sum=0
print("0 1 ",end='')
for i in range(0,n+1):
    sum=a+b
    a=b
    b=sum
    print(sum,end=' ')
