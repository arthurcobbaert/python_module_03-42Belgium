import math


def parse_tuple(coord: str, init_pos: tuple[int, int, int]) -> None:
    split_coord: list[str] = coord.split(",")
    int_list: list[int] = []
    length: int = 0
    try:
        for i in split_coord:
            int_list.append(int(i))
            length += 1
        if length == 3:
            tuple_coord: tuple[int, int, int] = tuple(int_list)
            print(f'\nParsing coordinates: "{coord}"')
            print(f"Parsed position: {tuple_coord}")
            (x, y, z) = tuple_coord
            dist: float = math.sqrt(
                (x - init_pos[0])**2
                + (y - init_pos[1])**2
                + (z - init_pos[2])**2
            )
            print(f"Distance between {init_pos} and {tuple_coord}: {dist:.1f}")
            print("\nUnpacking demonstration:")
            print(f"Player at x={x}, y={y}, z={z}")
            print(f"Coordinates: X={x}, Y={y}, Z={z}")
        else:
            raise ValueError
    except ValueError as e:
        print(f'\nParsing invalid coordinates: "{coord}"')
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: ValueError, Args: ({e})")


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    init_pos: tuple[int, int, int] = (0, 0, 0)
    pos: tuple[int, int, int] = (10, 20, 5)
    distance: float = math.sqrt(
            (pos[0] - init_pos[0])**2
            + (pos[1] - init_pos[1])**2
            + (pos[2] - init_pos[2])**2
    )
    print(f"\nPosition created: {pos}")
    print(f"Distance between {init_pos} and {pos}: {distance:.2f}")
    coord: str = "3,4,0"
    parse_tuple(coord, init_pos)
    invalid_coord: str = "abc,def,ghi"
    parse_tuple(invalid_coord, init_pos)
