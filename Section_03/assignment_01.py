# Assignment 1:
"""
    Create a function named merge_lists that accepts 2 lists.
    The function is supposed to merge both of those lists together
    and return the result.
"""

# your code below:

def merge_lists(list1, list2):
    new_list = list1 + list2
    return new_list


a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
print(merge_lists(a, b))





































# solution Below:

# def merge_lists(list_a, list_b):
#     return list_a + list_b
#
# my_list = merge_lists([1,2,3],['a', 'b', 'c'])
# print(my_list)