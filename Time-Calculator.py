# -*- coding: utf-8 -*-
"""
Created on Thu May 25 09:37:23 2023

@author: mrpot
"""

def main():
    seconds = int(input('Enter your desire seconds: '))
    print( seconds,'seconds', '=', timeCal(seconds))

def timeCal(secs):
    seconds = 0
    minutes = 0
    hours = 0
    days = 0
    if secs >= 60 and secs < 3600:
        minutes += secs // 60 
        return str(minutes) + ' min'
    elif secs >= 3600 and secs < 86400:
        hours += secs//3600
        minutes += (secs % 3600)//60 
        return str(hours) + 'h ' + str(minutes) + ' min'
    elif secs >= 86400:
        days += secs/86400
        return str(days) + ' days'
    else:
        return str(secs) + 's'

main()
            