import random

if __name__ == "__main__":
    players: list[str] = [
                "Alice",
                "bob",
                "Charlie",
                "dylan",
                "Emma",
                "Gregory",
                "john",
                "kevin",
                "Liam"
    ]
    print("=== Game Data Alchemist ===\n")
    print(f"Initial list of players: {players}")
    all_cap: list[str] = [p.capitalize() for p in players]
    print(f"New list with all names capitalized: {all_cap}")
    original_cap: list[str] = [p for p in players if p[0].isupper()]
    print(f"New list of capitalized names only: {original_cap}")
    score_dict: dict[str, int] = {
        name: random.randint(1, 1000) for name in all_cap
    }
    print(f"Score dict: {score_dict}")
    avg_score: float = sum(score_dict.values()) / len(score_dict)
    print(f"Score average is {avg_score:.2f}")
    high_scores: dict[str, int] = {
        name: score for name, score in score_dict.items() if score > avg_score
    }
    print(f"High scores: {high_scores}")
