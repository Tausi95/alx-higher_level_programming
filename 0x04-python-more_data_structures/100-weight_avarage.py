#!/usr/bin/python3

def weight_average(my_list=[]):
    """
    Calculate the weighted average of integers in tuples.
    Returns the weighted average or 0 if the list is empty.
    """
    if not my_list:
        return 0

    total_sum = 0
    total_weight = 0

    for score, weight in my_list:
        total_sum += score * weight
        total_weight += weight

    if total_weight == 0:
        return 0

    weighted_average = total_sum / total_weight
    return weighted_average

