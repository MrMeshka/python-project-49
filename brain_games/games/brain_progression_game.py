import random

RULES = 'What number is missing in the progression?'


def generate_random_number():
    min_value = 0
    max_value = 100
    return random.randint(min_value, max_value)


def generate_random_length():
    min_value = 5
    max_value = 10
    return random.randint(min_value, max_value)


def generate_start(length):
    max_value = 100
    steps_count = length - 1
    max_start = max_value - steps_count
    return random.randint(0, max_start)


def generate_step(start, length):
    max_value = 100
    steps_count = length - 1
    max_step = (max_value - start) // steps_count
    return random.randint(1, max_step)


def create_progression():
    length = generate_random_length()
    start = generate_start(length)
    step = generate_step(start, length)
    progression = ""
    for index in range(length):
        number = start + index * step
        number = str(number)
        if index != 0:
            number = " " + number
        progression += number
    return progression


def generate_round():
    progression = create_progression()
    numbers = progression.split()
    random_index = random.randint(0, len(numbers) - 1)
    random_number = numbers[random_index]
    numbers[random_index] = ".."
    progression = " ".join(numbers)
    return progression, random_number