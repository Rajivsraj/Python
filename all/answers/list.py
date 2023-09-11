"""
Python LIST Questions
======================================
    1. Python program to interchange first and last elements in a list
    2. Python program to swap two elements in a list
    3. Python | Ways to find length of list
    4. Maximum of two numbers in Python
    5. Minimum of two numbers in Python
"""

# 1. Python program to interchange  first and last elements in a list
lst = [3, 34, 45, 34, 45]
print(lst)

first = lst[0]
last = lst[len(lst)-1]

lst[0] = last
lst[len(lst)-1] = first
print(lst)