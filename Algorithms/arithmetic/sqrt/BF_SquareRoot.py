def sqrt(num):
    if num == 1 or num == 0:
        return num

    i = result = 1
    while result <= num:
        i += 1
        result = i * i

    return i - 1


print(sqrt(16))  # 4
print(sqrt(11))  # nearly 3
