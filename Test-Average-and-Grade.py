# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 15:34:50 2023

@author: mrpot
"""

def main():
    print('Your grade is:', determine_grade(calc_average()))

def calc_average():
    sum_scores = 0
    count = 0
    avg_scores = 0
    for scores in range(0, 5):
        scores = int(input('Enter the scores: '))
        if scores < 0 or scores > 100:
            print('Invalid scores')
        sum_scores +=scores
        count += 1
    
    avg_scores = sum_scores/count
    print('--------------------------\nYour average score is:', avg_scores)
    
    return avg_scores

def determine_grade(calc_average):
    if calc_average <= 100 and calc_average >= 90:
        return 'A'
    elif calc_average < 90 and calc_average >= 80:
        return 'B'
    elif calc_average < 80 and calc_average >= 70:
        return 'C'
    elif calc_average < 70 and calc_average >= 60:
        return 'D'
    else:
        return 'F'

main()