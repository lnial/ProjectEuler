#!/usr/bin/env python
# -*- coding: utf-8 -*-


START_YEAR = 1990

class Year(object):
    """class documentation"""
    def __init__(self, year, day):
        """set my year"""
        self.year = year
        if year == START_YEAR:
            self.start_day = 0
        else:
            self.start_day = day
        self.end_day = self._cal_end_day(self.start_day)

    def _sum_days(self):
        """return sum days"""
        if self.year % 400 != 0 and self.year % 100 == 0:
            return 365
        elif self.year % 4 == 0:
            return 366
        else:
            return 365
        
    def _cal_end_day(self, day):
        """cal end day"""
        return (self._sum_days() % 7 + 1 + day) % 7


    def end_of_day(self):
        """return end of day"""
        return self.end_day


    def retunr_count(self):
        """function documentation"""
        return self.count





if __name__ == '__main__':
    list_year = []
    end_of_day = 0
    for i in range(START_YEAR, 2001):
        y = Year(i, end_of_day)
        end_of_day = y.end_of_day()
        list_year.append(y)
    
    for i in list_year:
        print i.end_of_day()

