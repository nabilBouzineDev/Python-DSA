from Algorithms.search.wrapper import printer

"""
    Time Complexity is O(log(n)); since we divide recursively by a constant 2
"""


def search(my_list, target, start=None, last=None):
    while start <= last:
        mid = start + (last - start) // 2
        mid_value = my_list[mid]

        if mid_value == target:
            return target
        elif target > mid_value:
            start = mid + 1
        else:
            last = mid - 1

    return -1


list_one = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
printer(search(list_one, 10, 0, len(list_one) - 1))
