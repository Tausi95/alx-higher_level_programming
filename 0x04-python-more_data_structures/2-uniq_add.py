#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
    Add all unique integers in the list and return the sum.
    """
    # Create an empty set to store unique integers
    unique_set = set()
    
    # Sum up the unique integers
    total = 0
    for num in my_list:
        if num not in unique_set:
            unique_set.add(num)
            total += num
    
    return total

