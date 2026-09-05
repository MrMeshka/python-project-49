import random

RULES = 'What is the result of the expression?'

MAX_WINS = 3


def generate_random_number():
    min_value = 0
    max_value = 100
    return random.randint(min_value, max_value)


def generate_random_operator():
    operators = ['+', '-', '*']
    return random.choice(operators)


def get_result(number_a, operator, number_b):
    match operator:
        case '+':
            return number_a + number_b
        case '-':
            return number_a - number_b
        case '*':
            return number_a * number_b


def generate_round():
    number_a = generate_random_number()
    number_b = generate_random_number()
    operator = generate_random_operator()
    expression = f'{number_a} {operator} {number_b}'
    result = str(get_result(number_a, operator, number_b))
    return expression, result

    
