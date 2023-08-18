#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """
    Replace all occurrences of a specific element with another element in a new list.
    Returns a new list with replacements.
    """
    new_list = [replace if item == search else item for item in my_list]

    return new_list

