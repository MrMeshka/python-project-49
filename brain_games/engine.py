import prompt

from brain_games.cli import welcome_user


def game_engine(rules, max_wins, generate_round):
    name = welcome_user()
    print(rules)
    questions_count = 0
    while questions_count < max_wins:
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
    if questions_count == max_wins:
        print(f'Congratulations, {name}!')