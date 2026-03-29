import random


def gen_event(actions: list[str], players: list[str]) -> tuple:
    while True:
        random_action: str = random.choice(actions)
        random_player: str = random.choice(players)
        yield (random_player, random_action)


def consume_event(event_list: list[tuple[str, str]]):
    while True:
        random_event: tuple[str, str] = random.choice(event_list)
        yield random_event


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    actions: list[str] = [
            "run",
            "eat",
            "sleep",
            "grab",
            "run",
            "move",
            "climb",
            "swim"
    ]
    players: list[str] = ["bob", "alice", "dylan", "charlie"]
    event_stream = gen_event(actions, players)
    for i in range(1000):
        action, player = next(event_stream)
        print(f"Event {i}: Player {player} did action {action}")
    ten_events: list[tuple[str, str]] = []
    for _ in range(10):
        result: tuple[str, str] = next(event_stream)
        ten_events.append(result)
    print(f"Built list of 10 events: {ten_events}")
    event_consume = consume_event(ten_events)
    while len(ten_events) > 0:
        exclude: tuple[str, str] = next(event_consume)
        print(f"Got event from list: {exclude}")
        ten_events.remove(exclude)
        print(f"Remains in list: {ten_events}")
