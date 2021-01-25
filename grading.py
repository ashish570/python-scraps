#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function accepts a list of grades which are number.
# The function return a list of numbers with below logic:
#   If the difference between the grade  and the next multiple 5 of  is less than 3 , round  grade up to the next multiple of 5 .
#   If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade..
#

def gradingStudents(grades):
    fin_grades = []
    for grade in grades:
        if grade < 38 or grade %5 < 3:
            fin_grades.append(grade)
        else:
            fin_grades.append(5 * round(grade/5))
    return fin_grades

grades = [34,79,56,55,70]
final_grades = gradingStudents(grades)
print(final_grades)