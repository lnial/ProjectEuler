def factorial(x):
  if x == 0:
    return 0
  else:
    return x + factorial(x - 1)
 
def factorialRaise(x):
  y = x**2
  if y == 0:
    return 0
  else:
    return y + factorialRaise(x - 1)

factorialSum = factorial(100)
factorialSum = factorialSum **2
#print factorialSum

#print factorialRaise(100)
print factorialSum - factorialRaise(100)
