debug = 1
primFactor = 13195
list1 = []
list1.append(1)

for i in range(2, primFactor):

    print i
    if primFactor % i == 0:
        print i
        for j in list1:
            print list1
            #print j
            if list1[0] == 1:
                print 'ok'
                list1.append(i)
            elif j % i == 0:
                #print 'OK'
                break
            else:
                #print i
                #print "@@@@"
                list1.append(i)
    elif debug == 1:
        break
       
print list1

