

#Prime return 1
#not Prime 0
def isprime(n):
  if n < 2:
    return 0
  elif n == 2:
    return 1
  if n % 2 == 0 or n % 3 == 0:
    return 0

  i = 1
  while 1:

    #end condition
    if i * i  <= n:
      break
    i += 2
    if n % i == 0:
      print "OK"
      return 0

  return 1

print isprime(4)
#j = 1
#array = []

#while 1:
  #j += 1
  #if isprime(j):
    #array.append(j)
  #if len(array) == 1001:
    #break

#for k in array:
  #print k



#def primeNum(x):
#  # generate Prime List
#  list1 = [1, 2]
#  
#  return list1[x - 1]
#
##print primeNum(1)
#
#i = 1
#flag = 0
#listPrime = [2, 3, 5]
#while 1:
#  i += 1
#
#  checkFlag = 0
#  for j in listPrime:
#    if i % j != 0 and checkFlag == 0:
#      checkFlag = 1
#
#      if len(listPrime) == 6:
#        flag = 1
#        break
#  if checkFlag == 1:
#    listPrime.append(i)
#
#  if flag == 1:
#    break
#
#print listPrime
