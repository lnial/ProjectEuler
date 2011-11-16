#!/usr/bin/env python
# -*- coding: utf-8 -*-


next_index = 0
sumn = 0

for line in open('input18.txt', 'r'):
    line_arr = line[:-1].split(" ")

    if len(line_arr) != 1:
        print line_arr[next_index], line_arr[next_index + 1]
        next_index = line_arr.index(max(line_arr[next_index], line_arr[next_index + 1]))
        sumn += int(line_arr[next_index])
        "next_i" + str(next_index)

    else:
        sumn += int(line_arr[0])
        

print sumn
    



