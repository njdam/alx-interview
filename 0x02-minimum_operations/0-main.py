#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = -4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 1.5
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 15
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 17
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
