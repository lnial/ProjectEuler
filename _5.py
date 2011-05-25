
quotient = 10
flagEnd = 0
while 1:
  quotient += 1
  for i in range(1, 11):
      flagCount = 0
      if quotient % i == 0:
          flagCount += 1
          if flagCount == 10:
            flagEnd = 1
            print quotient
  if flagEnd == 1:
      break


