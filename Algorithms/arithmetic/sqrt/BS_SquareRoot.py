# Since we loop through ordered numbers,
# we can optimize our algorithm using Binary Search.

def binary_search_sqrt(num):

    if num == 1 or num == 0:
        return num

    # Initialize the search range
    start = 1
    end = num
    answer = None

    while start <= end:

        mid = (end + start) // 2
        if mid * mid == num:
            return mid

        if mid * mid < num:
            start = mid + 1
            answer = mid
        else:
            end = mid - 1

    return answer


print(binary_search_sqrt(16))  # 4
print(binary_search_sqrt(11))  # nearly 3
