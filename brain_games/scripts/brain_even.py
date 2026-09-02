import random

import prompt

from brain_games.cli import welcome_user


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    # Игра завершается после 3 правильных ответов, либо после 1 неправильного
    questions_count = 0
    while questions_count < 3:
        number = generate_random_number()
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        if check_answer(number, answer):
            questions_count += 1
            print('Correct!')
        else:
            # Пришлось ввести cor, т.к. линтер ругался на длинную строку
            cor = correct_answer(number)
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{cor}'.")
            print(f"Let's try again, {name}")
            break
    if questions_count == 3:
        print(f'Congratulations, {name}!')


def correct_answer(number):
    if is_even(number):
        return "yes"
    else:
        return "no"


def generate_random_number():
    min_value = 0
    max_value = 100
    return random.randint(min_value, max_value)


def is_even(number):
    return number % 2 == 0


def check_answer(number, answer):
    return correct_answer(number) == answer