import random

def get_random(number=3):
    if type(number) != int or number < 1 or number > 100:
        raise Exception("Invalid Data!")

    numbers = []

    while len(numbers) < number:
        n = random.randint(1, 100)
        if n not in numbers:
            numbers.append(n)

    numbers.sort()
    return numbers


# Examples
print(get_random(5))
print(get_random())