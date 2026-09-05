import random

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
MAX_WINS = 3


def generate_random_number():
    min_value = 0
    max_value = 100
    return random.randint(min_value, max_value)


def is_even(number):
    return number % 2 == 0


def generate_round():
    number = generate_random_number()
    if is_even(number):
        answer = "yes"
    else:
        answer = "no"
    return number, answer