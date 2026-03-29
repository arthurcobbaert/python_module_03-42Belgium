import math


def get_player_pos() -> tuple[float, float, float]:
    print("\nGet set of coordinates")
    while True:
        user_res = input("Enter new coordinates as floats in format 'x,y,z': ")
        numbers = user_res.split(",")
        if len(numbers) != 3:
            print("Invalid input")
            continue
        try:
            x = float(numbers[0])
            y = float(numbers[1])
            z = float(numbers[2])
            return (x, y, z)
        except ValueError as e:
            print(f"Error on parameter: {e}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    first_coord = get_player_pos()
    x, y, z = first_coord
    print(f"Got a first tuple: {first_coord}")
    print(f"It includes: X={x}, Y={y}, Z={z}")
    center: tuple[int, int, int] = (0, 0, 0)
    a, b, c = center
    distance_center: float = math.sqrt((x - a)**2 + (y - b)**2 + (z - c)**2)
    print(f"Distance to center: {distance_center:.4f}")
    second_coord = get_player_pos()
    x2, y2, z2 = second_coord
    distance: float = math.sqrt((x2 - x)**2 + (y2 - y)**2 + (z2 - z)**2)
    print(f"Distance between the 2 sets of coordinates: {distance:.4f}")
