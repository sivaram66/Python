Available = 10
x = int(input("How many Candies You want?"))
i = 1
while i <=x:
  if i > Available:
    print("out of stock")
    break
  print("Candy")
  i = i+1
  