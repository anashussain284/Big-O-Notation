"""
The program illustrates quadratic time complexity, executing a nested loop that
runs 'n' times for each 'n' iteration. Mathematically, this results in 
O(n) * O(n) = O(n * n), translating to a time complexity of O(n^2). In simpler
terms, the execution time grows quadratically with the size of the input, indicating
a less efficient algorithm for larger datasets.
"""

def square_with_same_input(n):
    for i in range(n):     # O(n)
        for j in range(n): # O(n)
            print(i, j)
print("1st start")
square_with_same_input(5)
print("1st end")
            
"""
COMMON MISTAKE

When running the nested for loop with two different values, the time complexity 
of the program is not O(n^2) since both inputs are distinct. Instead, it runs 'x'
times for each iteration of the outer loop and 'y' times for each iteration of the
inner loop. Consequently, the time complexity is expressed as O(x) * O(y) = O(x * y),
indicating that the execution time grows proportionally to the product of the two
input sizes 'x' and 'y'. In this scenario, the time complexity is O(xy)
"""

def square_with_different_input(x, y):
    for i in range(x):     # O(x)
        for j in range(y): # O(y)
            print(i, j)

print("2nd start")
square_with_different_input(5, 2)
print("2nd end")