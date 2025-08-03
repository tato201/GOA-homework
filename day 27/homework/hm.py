# 1
def remove_first_last(chars):
    return chars[1:-1]

# 2
def multiply_sums(list1, list2):
    sum1 = 0
    sum2 = 0
    for num in list1:
        sum1 += num
    for num in list2:
        sum2 += num
    return sum1 * sum2

# 3
def double_numbers(numbers):
    i = 0
    doubled = []
    while i < len(numbers):
        doubled.append(numbers[i] * 2)
        i += 1
    return doubled

# 4
def filter_even_numbers(numbers):
    evens = []
    for num in numbers:
        if num % 2 == 0:
            evens.append(num)
    return evens

# 5
def names_starting_with_n(names):
    n_names = []
    for name in names:
        if name.startswith("N"):
            n_names.append(name)
    return n_names



