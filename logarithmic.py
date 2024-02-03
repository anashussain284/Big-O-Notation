"""
BINARY SEARCH

The program showcases logarithmic time complexity, specifically exemplified in
the context of a binary search algorithm. With a time complexity of O(log n), 
the efficiency of the program increases as the input size grows. This logarithmic
behavior stems from the algorithm's ability to halve the search space at each step,
making it highly efficient for large datasets. In summary, the program's time
complexity follows a logarithmic growth pattern, offering optimal performance,
especially in scenarios involving sorted data
"""

def binary_search(list_1, start, end, target): # O(log n)
    mid = (start + end) // 2 # find the middle index of the input list
    if start > end: # If start index is bigger than end index, target value is not found
        return False
    elif target == list_1[mid]: # Target value is found
        return True
    elif target < list_1[mid] : # The target value is expected to reside on the left side of the middle index within the list.
        return binary_search(list_1, start, mid - 1, target)
    else: # The target value is expected to reside on the right side of the middle index within the list.
        return binary_search(list_1, mid + 1, end, target)
    

list_1 = [1, 112, 3, -4, 5, 6,17, 8]
list_1 = sorted(list_1)
start = 0
end = len(list_1) - 1
target = 17

print(binary_search(list_1, start, end, target))