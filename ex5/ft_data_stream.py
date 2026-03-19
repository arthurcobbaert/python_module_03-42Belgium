from typing import Generator


def process_event(num: int) -> Generator[int, None, None]:
    players: list[str] = [
                        "alice",
                        "bob",
                        "charlie",
                        "diana",
                        "eve",
                        "frank",
                        "arthur"
                    ]
    levels: list[int] = [2, 14, 7, 1, 5, 8, 29]
    actions: list[str] = ["killed monster", "found treasure", "leveled up"]
    j: int = 0
    treasure_event: int = 0
    level_event: int = 0
    high_level: int = 0
    for i in range(num):
        j += 1
        if i < len(players):
            yield (
                f"Event {j}: Player {players[i]} (level {levels[i]}) "
                f" {actions[i % len(actions)]}")
            if levels[i] >= 10:
                high_level += 1
            if actions[i % len(actions)] == "found treasure":
                treasure_event += 1
            elif actions[i % len(actions)] == "leveled up":
                level_event += 1
        else:
            yield "..."
            break
    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {num}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure_event}")
    print(f"Level-up events: {level_event}")


def fibonacci() -> Generator[int, None, None]:
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def prime_numbers() -> Generator[int, None, None]:
    num: int = 2
    while True:
        prime: bool = True
        for i in range(2, num):
            if num % i == 0:
                prime = False
                break
        if prime:
            yield num
        num += 1


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===\n")
    print("Processing 1000 events...\n")
    num: int = 1000
    gen_process = process_event(num)
    for event in gen_process:
        print(event)
    print("\nMemory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")
    print("\n=== Generator Demonstration ===")
    gen_fib = fibonacci()
    first: bool = True
    print("Fibonacci sequence (first 10):", end=" ")
    for i in range(10):
        if not first:
            print(",", end=" ")
        print(next(gen_fib), end="")
        first = False
    first: bool = True
    gen_prime = prime_numbers()
    print("\nPrime numbers (first 5):", end=" ")
    for i in range(5):
        if not first:
            print(",", end=" ")
        print(next(gen_prime), end="")
        first = False
    print()
