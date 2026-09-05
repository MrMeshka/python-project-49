import random

RULES = 'Find the greatest common divisor of given numbers.'


def generate_random_number():
    min_value = 0
    max_value = 100
    return random.randint(min_value, max_value)


def get_gcd(number_a, number_b):
    if number_b == 0:
        return number_a
    else:
        while number_b != 0:
            remainder = number_a % number_b
            number_a = number_b
            number_b = remainder
        return number_a


def generate_round():
    number_a = generate_random_number()
    number_b = generate_random_number()
    given_numbers = f'{number_a} {number_b}'
    result = str(get_gcd(number_a, number_b))
    return given_numbers, result
