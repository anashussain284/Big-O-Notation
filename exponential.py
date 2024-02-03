"""
EXPONENTIAL TIME COMPLEXITY [FIBONACCI SERIES]
----------------------------------------------
The time complexity of the given Fibonacci program is exponential, O(2^n),
due to its recursive approach. The function calls itself twice for each value
of 'n', resulting in a binary tree-like structure with approximately 2^n nodes.
This leads to inefficient performance as 'n' increases
"""

def fib(n):
    if n == 0:
        return 0 
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

print(fib(5))