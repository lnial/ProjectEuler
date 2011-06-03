
def primeNum(x):
  # generate Prime List
  list1 = [1, 2]
  
  return list1[x - 1]

#print primeNum(1)

i = 1
flag = 0
listPrime = [2, 3, 5]
while 1:
  i += 1

  checkFlag = 0
  for j in listPrime:
    if i % j != 0 and checkFlag == 0:
      checkFlag = 1

      if len(listPrime) == 6:
        flag = 1
        break
  if checkFlag == 1:
    listPrime.append(i)

  if flag == 1:
    break

print listPrime
