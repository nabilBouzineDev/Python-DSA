from wrapper import is_sorted


# T.C is O(n2)
def sort(my_list):
    size = len(my_list)
    # Loop through the list
    for i in range(size):
        for j in range(size - i - 1):
            if my_list[j] > my_list[j + 1]:
                # Swap unordered adjacent
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    return my_list


list_one = [0, 1, 2, 34, 100, 4, 53, -1]
sorted_list = sort(list_one)
print(is_sorted(sorted_list))
