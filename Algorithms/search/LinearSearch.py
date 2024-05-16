from wrapper import printer

"""
    Time Complexity is O(n); where n is the size of the input.
"""


def search(my_list, target):
    for value in my_list:
        if value == target:
            return value
    return -1


list_one = [0, 1, 2, 34, 100, 4, 53, -1]

printer(search(list_one, 0))
printer(search(list_one, 9))
