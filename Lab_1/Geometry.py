__author__ = 'Yonglin'
'''This file Geometry.py will help us practice some function concepts'''
from math import pi
# Question_a: Write a function CircleArea(radius) that computes the area of a circle
#def CircleArea(radius):
#    area = pi*radius**2
#    return area

# Question_b: Modify the CircleArea function so that it checks it the radius is positive
def CircleArea(radius):
    '''CircleArea is used for computing the area of a circle'''

    if radius < 0:
        print('The radius must be positive')
        return None
    else:
        area = pi*radius**2
        return area


# Question_c: Now write another function RectangleArea

def RectangleArea(base, height):
    '''Computes the area of a rectangle'''
    if base < 0 or height < 0:
        print('The base and height must be positive')
    else:
        area = base * height
        return area
# add the pythonpath on Ubuntu
# import sys
# sys.path.append("/home/yonglin/PycharmProjects/TextMining_Lab_1")

# Question_d : Now define another function in your Geometry module
def TriangleArea(base, height):
    '''Computes the area of a rectangle'''
    if base < 0 or height < 0:
        print('The base and height must be positive')
    else:
        area = 0.5 * base * height
        return area
# The reason why we cannot import the new function is that we just added the PYTHONPATH temporarily not permanently