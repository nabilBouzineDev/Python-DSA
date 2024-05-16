from wrapper import is_sorted


# T.C is O(nlog(n))
# It's best option when we're dealing with an external large data set.

def merge_sort(my_list):
    if len(my_list) > 1:
        mid = len(my_list) // 2
        left_part = my_list[:mid]
        right_part = my_list[mid:]

        # Divides recursively into two parts
        merge_sort(left_part)
        merge_sort(right_part)

        # Merge and copy parts in order in a list
        l = r = k = 0
        while l < len(left_part) and r < len(right_part):
            if left_part[l] < right_part[r]:
                my_list[k] = left_part[l]
                l += 1
            else:
                my_list[k] = right_part[r]
                r += 1
            k += 1

        # Add remaining elements into the list
        while l < len(left_part):
            my_list[k] = left_part[l]
            l += 1
            k += 1

        while r < len(right_part):
            my_list[k] = right_part[r]
            r += 1
            k += 1

    return my_list


list_one = [12, 11, 13, 5, 6, 7]
sorted_list = merge_sort(list_one)
print(is_sorted(sorted_list))
