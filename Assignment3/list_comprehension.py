"""
program to find all numbers divisible by 5 between (2000 and 3000)
and insert those elements in a list and then print them.
"""

list = [m for m in range(2000,3000) if m % 5 == 0]
print list