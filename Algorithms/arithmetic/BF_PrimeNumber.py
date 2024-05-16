# T.C is O(n)

def is_prime_number(num):
    # Handle specific case
    if num <= 1:
        return False

    for i in range(2, num - 1):
        if num % i == 0:
            return False
    return True


print(is_prime_number(5))  # True
print(is_prime_number(6))  # False
