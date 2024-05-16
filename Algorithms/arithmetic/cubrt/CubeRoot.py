def calculate_error(num, mid):
    if num < (mid ** 3):
        return (mid ** 3) - num
    else:
        return num - (mid ** 3)


def bs_cubic_root(num):
    # handle specific cases
    if num == 0 or num == 1:
        return num

    # Set initial ranges
    start = 0
    end = num

    # Set the precision number
    e = 0.0000001

    while True:
        mid = (start + end) / 2
        error = calculate_error(num, mid)

        # the loop won't break until this is true
        if error <= e:
            return round(mid)

        if mid ** 3 > num:
            end = mid
        else:
            start = mid


print(bs_cubic_root(27))  # 3
print(bs_cubic_root(8))  # 2
