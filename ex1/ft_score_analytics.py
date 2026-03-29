import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    argv: list[str] = sys.argv
    scores: list[int] = []
    total_score: int = 0
    total_players: int = 0
    try:
        if len(argv) == 1:
            raise ValueError(
                f"No scores provided. Usage: python3 {argv[0]} "
                "<score1> <score2> ..."
            )
        for arg in argv[1:]:
            try:
                score: int = int(arg)
                total_score += score
                scores = scores + [score]
                total_players += 1
            except ValueError:
                print(f"Invalid parameter: {arg}")
        if total_players == 0:
            print("Error: No valid numerical scores were provided.")
        else:
            average: float = total_score / total_players
            highest: int = max(scores)
            lowest: int = min(scores)
            rng: int = highest - lowest
            print(f"Scores processed: {scores}")
            print(f"Total players: {total_players}")
            print(f"Total score: {total_score}")
            print(f"Average score: {average:.1f}")
            print(f"High score: {highest}")
            print(f"Low score: {lowest}")
            print(f"Score range: {rng}")
    except ValueError as e:
        print(f"{e}")
