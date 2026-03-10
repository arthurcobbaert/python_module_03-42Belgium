def list_comprehension(data: list[dict]) -> None:
	high_scores: list[str] = []
	doubled_scores: list[int] = []
	active: list[str] = []
	print("High scores (>2000):", end=" ")
	for player in data:
		if player["score"] > 2000:
			high_scores.append(player["name"])
	print(high_scores)
	print("Scores doubled:", end=" ")
	for player in data:
		double: int = player["score"] * 2
		doubled_scores.append(double)
	print(doubled_scores)
	print("Active players:", end=" ")
	for player in data:
		if player["status"] == "active":
			active.append(player["name"])
	print(active)
def dict_comprehension(data: list[dict]) -> None:
	scores: dict[str, int] = {}
	high: int = 0
	medium: int = 0
	low: int = 0
	print("Players scores:", end=" ")
	for player in data:
		if player["status"] == "active":
			scores[player["name"]] = player["score"]
	print(scores)
	categories: dict[str, int] = {
			"high": 0,
			"medium": 0,
			"low": 0,
	}
	print("Score categories:", end=" ")
	for player in data:
		if player["status"] == "active":
			if player["score"] > 2000:
				categories["high"] += 1
			elif player["score"] >= 1500:
				categories["medium"] += 1
			else:
				categories["low"] += 1
	print(categories)
	count: dict[str, int] = {}
	print("Achievement counts: ", end=" ")
	for player in data:
		j: int = 0
		if player["status"] == "active":
			for i in player["achievements"]:
				if player["achievements"] != "":
					j += 1
			count[player["name"]] = j
	print(count)
def set_comprehension(data: list[dict]) -> None:
	unique_players: set[str] = set()
	unique_achiev: set[str] = set()
	print("Unique players:", end=" ")
	for player in data:
		unique_players.add(player["name"])
	print(unique_players)
	print("Unique achievements:", end=" ")
	common_achiev: set[str] = set(data[0]["achievements"])
	for player in data[1:]:
		common_achiev = common_achiev.intersection(player["achievements"])
	print(common_achiev)
	regions: set[str] = set()
	for player in data:
		regions.add(player["region"])
	print(f"Active regions: {regions}")
	print("\n=== Combined Analysis ===")
	total_players: int = len(data)
	print(f"Total players: {total_players}")
	total_unique_achiev: int = len(common_achiev)
	print(f"Total unique achievements: {total_players * total_unique_achiev}")
	total_score: int = 0
	print("Average score:", end=" ")
	for player in data:
		total_score += player["score"]
	print(f"{total_score / total_players:.1f}")
	print("Top performer:", end=" ")
	top_performer: dict[str, any] = data[0]
	for player in data[1:]:
		if player["score"] > top_performer["score"]:
			top_performer = player
	name = top_performer["name"]
	score = top_performer["score"]
	len_achiev = len(top_performer["achievements"])
	print(f"{name} ({score} points, {len_achiev} acievements)")
if __name__ == "__main__":
	data: list[dict] = [
		{
			"name": "alice",
			"score": 2300,
			"status": "active",
			"achievements": ["first_kill", "level_10", "treasure_hunter", "speed_demon", "boss_slayer"],
			"status": "active",
			"region": "north",
		},
		{
			"name": "bob",
			"score": 1800,
			"status": "active",
			"achievements": ["first_kill", "level_10",  "boss_slayer", "collector"],
			"status": "active",
			"region": "east",
		},
		{
			"name": "charlie",
			"score": 2150,
			"achievements": ["treasure_hunter", "first_kill", "level_10", "boss_slayer", "speed_demon", "perfectionist"],
			"status": "active",
			"region": "north",
		},
		{
			"name": "diana",
			"score": 2050,
			"achievements": ["first_kill", "boss_slayer", "level_10"],
			"status": "inactive",
			"region": "central",
		},	
	]
	print("=== Game Analytics Dashboard ===\n")
	print("=== List Comprehension Examples ===")
	list_comprehension(data)
	print("\n=== Dict Comprehension Examples ===")
	dict_comprehension(data)
	print("\n=== Set Comprehension Examples === ")
	set_comprehension(data)
