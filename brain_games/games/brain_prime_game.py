import random

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_random_number():
    min_value = 0
    max_value = 100
    return random.randint(min_value, max_value)


def is_prime(number):
    if number < 2:
        return False
    for divisor in range(2, number):
        if number % divisor == 0:
            return False
    return True


def generate_round():
    number = generate_random_number()
    if is_prime(number):
        answer = "yes"
    else:
        answer = "no"
    return number, answer