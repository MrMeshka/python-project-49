from brain_games.engine import game_engine
from brain_games.games.brain_calc_game import MAX_WINS, RULES, generate_round


def main():
    game_engine(
        rules=RULES,
        max_wins=MAX_WINS,
        generate_round=generate_round
    )


if __name__ == "__main__":
    main()   