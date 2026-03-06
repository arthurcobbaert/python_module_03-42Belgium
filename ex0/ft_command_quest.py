import sys

if __name__ == "__main__":
	print("=== Command Quest ===")
	
	total_len: int = len(sys.argv)
	argv: list[str] = sys.argv
	if total_len == 1:
		print("No arguments provided!")
		print(f"Program name: {argv[0]}")
	else:
		print(f"Program name: {argv[0]}")
		total_args: int = total_len - 1
		print(f"Arguments received: {total_args}")
		i: int = 1
		while i <= total_args:
			print(f"Argument {i}: {argv[i]}")
			i += 1
	print(f"Total arguments: {total_len}")
