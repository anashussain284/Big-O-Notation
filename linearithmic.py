"""
MERGE SORT

The program exemplifies linearithmic time complexity, as seen in the example of
a merge sort implementation. In the merge sort program, there is an inner loop
with 'n' iterations, resulting in a time complexity of O(n). Additionally, there
is an outer loop with a time complexity of O(log n). Combining these complexities,
we get O(n) * O(log n) = O(n * log n), signifying a linearithmic growth in execution
time. Therefore, the overall time complexity of the program is expressed as O(n log n).

"""

def merge_sort(list_1): # Outer loop => O(log n)
    if len(list_1) < 2:
        return list_1
    
    mid_index = len(list_1) // 2
    left_list = list_1[:mid_index]
    right_list = list_1[mid_index:]

    return merge(merge_sort(left_list), merge_sort(right_list))

def merge(left_list, right_list): # Inner loop => O(n)
    result_list = []
    left_index = 0
    right_index = 0

    while (left_index < len(left_list) and right_index < len(right_list)):
        if (left_list[left_index] < right_list[right_index]):
            result_list.append(left_list[left_index])
            left_index += 1
        else:
            result_list.append(right_list[right_index])
            right_index += 1
    result_list.extend(left_list[left_index:])
    result_list.extend(right_list[right_index:])
    
    return result_list

list_1 = [12, 3, 16, 6, 5, 1]
print(f"befor sort-{list_1}")
print(f"after sort-{merge_sort(list_1)}")
