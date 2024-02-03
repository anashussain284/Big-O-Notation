"""
FACTORIAL TIME COMPLEXITY O(n!)
-------------------------------
Here's a Python program that exhibits factorial time complexity O(n!). The time
complexity of this program is O(n!), where 'n' is the length of the input list.
This is because, in the worst case, the program generates all possible permutations,
and the number of permutations is factorial in the size of the input list
"""    
def permute(input_list):
    def backtrack(start):
        if start == len(input_list) - 1:
            # Process the permutation (e.g., print or store it)
            print(input_list)
            return

        for i in range(start, len(input_list)):
            input_list[start], input_list[i] = input_list[i], input_list[start]
            backtrack(start + 1)
            input_list[start], input_list[i] = input_list[i], input_list[start]  # Backtrack

    backtrack(0)

input_list = [1, 2, 3]
permute(input_list)