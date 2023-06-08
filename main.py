fruits = ["apple", "banana", "cherry", "orange"]
vegetables = ["carrot", "cucumber"]

grocery = fruits + vegetables
print(grocery)

numbers = [10, 5, 8, 1, 7]
numbers.sort()
print(numbers)

slice_numbers = numbers[1:4]
print(slice_numbers)

alias_number = numbers
print(alias_number)

alias_number.pop()

print(numbers)

numbers_copy = numbers.copy()
numbers_copy.pop()
print('numbers_copy', numbers_copy)
print('numbers',numbers)


numbers_clone = numbers[:]
print(numbers_clone)


