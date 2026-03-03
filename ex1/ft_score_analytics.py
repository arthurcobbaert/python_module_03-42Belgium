import sys

if __name__ == "__main__":
	print("=== Player Score Analytics ===")

	argv = sys.argv
	scores = []
	total_score = 0
	total_players = 0
	i = 1
	try:
		if len(argv) == 1:
			raise ValueError(f"No scores provided. Usage: python3 {argv[0]} <score1> <score2> ...")
		for arg in argv[1:]:
			try:
				score = int(argv[i])
			except ValueError:
				raise ValueError(f"'{argv[i]}' is not a valid score!")
			total_score += score
			scores = scores + [score]
			i += 1
			total_players += 1
		average = total_score / total_players
		highest = max(scores)
		lowest = min(scores)
		rng = highest - lowest
		print(f"Scores processed: {scores}")
		print(f"Total players: {total_players}")
		print(f"Total score: {total_score}")
		print(f"Average score: {average:.1f}")
		print(f"High score: {highest}")
		print(f"Low score: {lowest}")
		print(f"Score range: {rng}")
	except ValueError as e:
		print(f"{e}")
		sys.exit(1)
