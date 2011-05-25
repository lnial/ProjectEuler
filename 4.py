
maxMulti = 0
for i in range(1000):
    for j in range(1000):
        multi = i * j
        if len( str(multi) ) == 6:
                listStr = list(str(multi))

                #partition element 
                if listStr[0] == listStr[5] and listStr[1] == listStr[4] and listStr[2] == listStr[3]:
                    if maxMulti < multi:
                        #print multi
                        maxMulti = multi
                             

print maxMulti

