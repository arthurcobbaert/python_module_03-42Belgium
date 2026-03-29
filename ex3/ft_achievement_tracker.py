import random


def gen_player_achievements():
    all_achiev: set[str] = {
                        'Crafting Genius',
                        'Strategist',
                        'World Savior',
                        'Speed Runner',
                        'Survivor',
                        'Master Explorer',
                        'Treasure Hunter',
                        'Unstoppable',
                        'First Steps',
                        'Collector Supreme',
                        'Untouchable',
                        'Sharp Mind',
                        'Boss Slayer'
    }
    alice: set[str] = set(random.sample(list(all_achiev), 4))
    bob: set[str] = set(random.sample(list(all_achiev), 8))
    charlie: set[str] = set(random.sample(list(all_achiev), 6))
    dylan: set[str] = set(random.sample(list(all_achiev), 9))
    print(f"Player Alice: {alice}\n")
    print(f"Player Bob: {bob}\n")
    print(f"Player Charlie: {charlie}\n")
    print(f"Player Dylan: {dylan}\n")
    all_distinct: set[str] = alice.union(bob).union(charlie).union(dylan)
    print(f"All distinct qchievements: {all_distinct}\n")
    common_achiev: set[str] = (
        alice.intersection(bob)
        .intersection(charlie)
        .intersection(dylan)
    )
    print(f"Common achievements: {common_achiev}")
    only_alice: set[str] = (
        alice.difference(bob)
        .difference(charlie)
        .difference(dylan)
    )
    only_bob: set[str] = (
        bob.difference(alice)
        .difference(charlie)
        .difference(dylan)
    )
    only_charlie: set[str] = (
        charlie.difference(alice)
        .difference(bob)
        .difference(dylan)
    )
    only_dylan: set[str] = (
        dylan.difference(alice)
        .difference(bob)
        .difference(charlie)
    )
    print(f"Only Alice has: {only_alice}")
    print(f"Only Bob has: {only_bob}")
    print(f"Only Charlie has: {only_charlie}")
    print(f"Only Dylan has: {only_dylan}\n")
    alice_missing: set[str] = all_achiev.difference(alice)
    bob_missing: set[str] = all_achiev.difference(bob)
    charlie_missing: set[str] = all_achiev.difference(charlie)
    dylan_missing: set[str] = all_achiev.difference(dylan)
    print(f"Alice is missing: {alice_missing}\n")
    print(f"Bob is missing: {bob_missing}\n")
    print(f"Charlie is missing: {charlie_missing}\n")
    print(f"Dylan is missing: {dylan_missing}")


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")
    gen_player_achievements()
