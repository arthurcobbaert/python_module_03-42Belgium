def track(name: str, data: set[str]) -> None:
	print(f"Player {name} achievements: {data}")

def check(set1: set[str], set2: set[str], set3: set[str]) -> None:
	all_unique: set[str] = set1.union(set2).union(set3)
	length: int = len(all_unique)
	print(f"All unique achievements: {all_unique}")
	print(f"Total unique achievements: {length}\n")
	all_common: set[str] = set1.intersection(set2).intersection(set3)
	print(f"Common to all players: {all_common}")
	alice_diff: set[str] = set1.difference(set2).difference(set3)
	bob_diff: set[str] = set2.difference(set1).difference(set3)
	charlie_diff: set[str] = set3.difference(set1).difference(set2)
	all_diff: set[str] = alice_diff.union(charlie_diff).union(bob_diff)
	print(f"Rare achievements (1 player): {all_diff}\n")
	common_alice_bob: set[str] = set1.intersection(set2)
	unique_alice: set[str] = set1.difference(set2)
	unique_bob: set[str] = set2.difference(set1)
	print(f"Alice vs Bob common: {common_alice_bob}")
	print(f"Alice unique: {unique_alice}")
	print(f"Bob unique: {unique_bob}")

if __name__ == "__main__":
	print("=== Achievement tracker system ===\n")
	alice: set[str] = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
	bob: set[str] = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
	charlie: set[str] = {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon', 'perfectionist'}
	track("alice", alice)
	track("bob", bob)
	track("charlie", charlie)
	print("\n=== Achievement Analytics ===")
	check(alice, bob, charlie)
