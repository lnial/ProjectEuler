#!/usr/bin/env python
# -*- coding: utf-8 -*-


next_index = 0
sumn = 0
line_dir = []

for line in open('input18.txt', 'r'):
    line_arr = line[:-1].split(" ")
    line_dir.append(line_arr)
    

    #if len(line_arr) != 1:
        #print line_arr[next_index], line_arr[next_index + 1]
        #next_index = line_arr.index(max(line_arr[next_index], line_arr[next_index + 1]))
        #sumn += int(line_arr[next_index])
        #"next_i" + str(next_index)

    #else:
        #sumn += int(line_arr[0])

for i in xrange(len(line_dir), 0 , -1):
    print line_dir[i-1], len(line_dir[i-1])
    for j in xrange(0, len(line_dir[i-1])):
        print line_dir[i-1][j]

    #for j in line_dir[i-1]:
        ##print line_dir[i-1][

        #print j


class tedhst():
    """class documentation"""
    def __init__(self, a):
        """__init__ documentation"""
        pass




