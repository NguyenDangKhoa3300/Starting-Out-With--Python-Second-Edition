# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 15:18:03 2023

@author: mrpot
"""

def main():
    for seconds in range(0, 10):
        print(seconds, ':', falling_distance(seconds))

def falling_distance(seconds):
    g = 9.8
    d = 1/2*g*pow(seconds, 2)
    return d

main()