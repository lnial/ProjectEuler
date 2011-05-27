quotient = 100
flagEnd = 0

#print len(list1)

#count = 1
#for i in range(1, 21):
  #count = count * i


while 1:
  quotient += 1
  count = 0

  for i in range(1, 21):
    if quotient % i == 0:
      count += 1
    if count == 20:
      flagEnd = 1
      break
  if flagEnd == 1:
    break

print quotient




#for i in range(1, 10):
  #print i



#quotient = 10
#flagEnd = 0
#while 1:
  #break
  #quotient += 1
  #for i in range(1, 11):
      #flagCount = 0
      #if quotient % i == 0:
          #flagCount += 1
          #if flagCount == 10:
            #flagEnd = 1
            #print quotient
  #if flagEnd == 1:
      #break

