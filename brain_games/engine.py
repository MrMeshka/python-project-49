import prompt

from brain_games.cli import welcome_user

MAX_WINS = 3


def game_engine(rules, generate_round):
    name = welcome_user()
    print(rules)
    questions_count = 0
    while questions_count < MAX_WINS:
        question, correct_answer = generate_round()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            questions_count += 1
            print('Correct!')
        else:
            print(
                f"'{answer}' is wrong answer ;(."
                f"Correct answer was '{correct_answer}'."
                )
            print(f"Let's try again, {name}")
            break
    if questions_count == MAX_WINS:
        print(f'Congratulations, {name}!')