numbers = [1, 2, 3, 4, 5]

print(numbers[2])
print(numbers)

for num in numbers:
    print(num)

numbers.append(6)
print(numbers)

# remove at index 01
numbers.pop(1)
print(numbers)

# remove element 1
numbers.remove(1)
print(numbers)
