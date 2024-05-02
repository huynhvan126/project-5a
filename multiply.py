# Author: Van Huynh
# GitHub username: huynhvan126
# Date: 05/01/2024
# Description: multiplies two positive integers using recursion and addition.
def multiply(a, b):
    """This function multiplies two positive integers using recursion and addition"""
    if b == 1: #base case:if b=1 return a
        return a
    return a + multiply(a, b-1)