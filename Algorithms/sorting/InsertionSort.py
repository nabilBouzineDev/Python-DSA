from wrapper import is_sorted


# T.C is O(n2)

def sort(my_list):
    for i in range(1, len(my_list)):
        for j in range(0, i):
            if my_list[i] < my_list[j]:
                my_list[i], my_list[j] = my_list[j], my_list[i]
    return my_list


list_one = [6, 5, 13, 11, 12]
sorted_list = sort(list_one)
print(is_sorted(sorted_list))
