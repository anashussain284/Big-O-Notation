"""
The program illustrates cubic time complexity, executing a nested loop that runs
'n' times for each 'n' iteration for 'n' iteration. Mathematically, this results
in O(n) * O(n) * O(n) = O(n * n * n), translating to a time complexity of O(n^3).
In simpler terms, the execution time grows cubically with the size of the input,
indicating a less efficient algorithm for larger datasets.
"""

def cube(n):
    for i in range(n):         # O(n)
        for j in range(n):     # O(n)
            for k in range(n): # O(n)
                print(i, j, k)

# cube(3)

"""
COMMON MISTAKE

When running the nested for loop with three different values, the time complexity
of the program is not O(n^3) since each inputs are distinct. Instead, it runs 'x'
times for each iteration of the outer most loop, 'y' times for each iteration of
the outer loop and 'z' times for each iteration of the inner loop. Consequently,
the time complexity is expressed as O(x) * O(y) * O(z) = O(x * y *z), indicating
that the execution time grows proportionally to the product of the three input 
sizes 'x', 'y' and 'z'. In this scenario, the time complexity is O(xyz)
"""

def cube(x, y, z):
    for i in range(x):         # O(x)
        for j in range(y):     # O(y)
            for k in range(z): # O(z)
                print(i, j, k)

cube(2, 3, 4)