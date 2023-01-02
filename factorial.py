n = eval(input("Enter the Number"))

def fac(n):
  if n ==0:
    return 1
  return n *fac(n-1)


result = fac(n)
print(result)