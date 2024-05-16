from wrapper import is_sorted


# T.C is O(n2) at the worst case.
# However, It's the faster among the sorting algo.

def partition(my_list, first, last):
    """
        This function takes the last element as a pivot
        It places elements less than pivot at the left
        It places elements greater than pivot at the right
        It places the pivot at the correct place.
        Returns index of the pivot.
    """

    i = (first - 1)
    pivot = my_list[last]

    for j in range(first, last):
        if my_list[j] <= pivot:
            i += 1
            my_list[j], my_list[i] = my_list[i], my_list[j]

    # Placing the pivot at the half and return its index.
    my_list[i + 1], my_list[last] = my_list[last], my_list[i + 1]
    return i + 1


def quick_sort(my_list, first, last):
    if first < last:

        pivot_idx = partition(my_list, first, last)

        # Sort other parts: left and right
        quick_sort(my_list, first, pivot_idx - 1)
        quick_sort(my_list, pivot_idx + 1, last)
    return my_list


list_one = [12, 11, 13, 5, 6, 7]
sorted_list = quick_sort(list_one, 0, len(list_one) - 1)
print(is_sorted(sorted_list))
