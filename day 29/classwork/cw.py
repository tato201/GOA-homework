def count_words(sentence):
    words = sentence.split()
    return len(words)


print(count_words("This is a simple sentence"))  


def sum_of_evens(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    return total

print(sum_of_evens([1, 2, 3, 4, 5, 6])) 

def max_number(numbers):
    if not numbers:
        return None 
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum

print(max_number([10, 25, 3, 48, 7])) 