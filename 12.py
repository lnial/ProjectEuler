#!/usr/bin/env python
# -*- coding: utf-8 -*-

def get_sum(n):
    """nまでsumし合計値を返す"""
    sum = 0
    for i in xrange(1, n + 1):
        sum += i
    #return sum
    return sum;



def get_divisor(n):
    list = []
    """input array"""
    if n == 1:
        return 1
    #print n
    for i in xrange(1, n + 1):
        if (n % i == 0):
            list.append(i)
    #print list
    return len(list) 


if __name__ == '__main__':

    CONST_NUMBER = 100010000

    #回答の個数
    ANSWER_NUMBER = 501
    for i in xrange(1, CONST_NUMBER + 1):
        tri = get_sum(i)
        if (get_divisor(tri) >= ANSWER_NUMBER):
            print tri
            break

    



#def fact(n, a = 1):
#  if n == 0:
#    return a
#  return fact(n-1, n*a)
#
#def num_of_divisor(num, iszero, divisor = 0):
#  if divisor == 3:
#    return iszero
#  print iszero
#
#  return num_of_divisor(num - 1, num * num)


#print num_of_divisor(4, 4)


#if __name__ == '__main__':
  #list = [0]
  #i = 0

  #while True:
    #i += 1
    #list.append(list[i-1] + i)
  
    #if i == 1000:
      #break
    ##list.append(int(list[i]) + i)
    ##if i == 1000:
      ##print list[i]
      ##break

  #print list[3]


