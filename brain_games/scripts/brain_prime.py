from brain_games.engine import game_engine
from brain_games.games.brain_prime_game import RULES, generate_round


def main():
    game_engine(
        rules=RULES,
        generate_round=generate_round
    )


if __name__ == "__main__":
    main()