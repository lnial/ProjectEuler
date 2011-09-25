#!/usr/bin/env python
# -*- coding: utf-8 -*-

def odd_fun(n):
    return 3 * n + 1

def even_fun(n):
    return n/2

def return_one(n):
    i = 1
    while n != 1:
        i += 1
        if n % 2 == 0:
            n = even_fun(n)
        else:
            n = odd_fun(n)
    return i



if __name__ == '__main__':

    i = 0
    list = [0]
    #i = 1000000
    while 1:
        i += 1
        if max(list) < return_one(i):
            max_num = i
            list.append(return_one(i))

        if i == 1000000:
        #if i == 100:
            break

    print max(list)
    print max_num


    #print list.index(max(list))

    #while i != 1:
        #i -= 1
        ##print return_one(i)
        #list.append(return_one(i))
        #print list

    #print max(list)

    #print max(list)
    #print ""
    #i = 0
    #for i in list:
        #print i

