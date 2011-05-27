quotient = 1L

while 1:
  flagEnd = 0
  for i in range(1, 21):
    flagEnd += (quotient % i)

  if flagEnd == 0:
    break
  quotient += 1
  print quotient

print quotient

#great
#def delbart(t,n):
  #if n > 0:
    #if not (t%n):
      #if delbart(t, n-1):
        #return True
      #else:
        #return False
    #else:
      #return False
  #else:
    #return True

#i = 20
#while not delbart(i,20):
  #i +=20

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

