debug = 1
primFactor = 13195
#primFactor = 600851475143L
list1 = []
list1.append(1)

for i in range(2, primFactor):

    if primFactor % i == 0:
      list1.append(i)
       

#dispose
list1.remove(1)
print list1
#list2 = list1[:]
#list1.reverse()
#print range(list1)

#for j in range(list1[0], list1):
  #print j
  #for k in range(list2):
    #if j % k == 0:
      #print "@@@"
      #list1.remove(j)
    

  

#print j
  #if  % j != 0:
    #list1.append(i)

