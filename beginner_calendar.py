#!/usr/bin/env python2.7
#coding: utf-8

import calendar

while True:
    print "Show a given years monthly calendar"
    year = int(raw_input("Enter the year: "))
    calendar.prcal(year)

    raw_input("Press enter to go on...")

