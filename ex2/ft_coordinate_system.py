import sys
import math

def parse_tuple(coord):
	split_coord = coord.split(", ")
	int_list = []
	try:
		for i in split_coord:
			int_list.append(int(i))
		if (len(int_list) == 3):
			tuple_coord = tuple(int_list)
			print(f'\nParsing coordinates: "{coord}"')
			print(f"Parsed position: {tuple_coord}")
		else:
			raise ValueError
	except ValueError as e:
		print(f'\nParsing invalid coordinates: "{coord}"')
		print(f"Error parsing coordinates: {e}")
		print(f"Error details - Type: ValueError, Args: ({e})")

if __name__ == "__main__":
	print("=== Game Coordinate System ===")
	pos = (10, 20, 5)
	init_pos = (0, 0, 0)
	distance = math.sqrt((pos[0] - init_pos[0])**2 + (pos[1] - init_pos[1])**2 + (pos[2] - init_pos[2])**2)
	print(f"\nPosition created: {pos}")
	print(f"Distance between {init_pos} and {pos}: {distance:.2f}")
	
	coord = "3, 4, 0"
	parse_tuple(coord)

	invalid_coord = "abc, def, ghi"
	parse_tuple(invalid_coord)
