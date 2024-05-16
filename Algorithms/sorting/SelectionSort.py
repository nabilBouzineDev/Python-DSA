from wrapper import is_sorted


# T.C is O(n2)

def sort(my_list):
    for i in range(len(my_list)):
        min_index = i
        for j in range(i + 1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        my_list[i], my_list[min_index] = my_list[min_index], my_list[i]

    return my_list


list_one = [0, 1, 2, 34, 100, 4, 53, -1]
sorted_list = sort(list_one)
print(is_sorted(sorted_list))
