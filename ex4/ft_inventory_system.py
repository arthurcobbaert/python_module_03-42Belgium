import sys


def get_perc(inventory: dict[str, int], total: int) -> None:
    perc: float = 0
    for key, value in inventory.items():
        perc = value * 100 / total
        print(f"Item {key} represents: {perc:.1f}%")


def get_stats(inventory: dict[str, int]) -> None:
    most: int = 0
    most_key: str = ""
    least: int = 0
    least_key: str = ""
    first: bool = True
    for key, value in inventory.items():
        if value > most:
            most = value
            most_key = key
        if first or value < least:
            least = value
            least_key = key
            first = False
    print(f"Item most abundant: {most_key} with quantity {most}")
    print(f"Item least abundant: {least_key} with quantity {least}")


def update_inventory(key: str, value: int, inventory: dict[str, int]) -> None:
    try:
        key = key + ""
        if key in inventory:
            print(f"Redundant item '{key}' - discarding")
            return
        num: int = int(value)
        inventory.update({key: num})
        print(f"Updated inventory: {inventory}")
    except ValueError as e:
        print(f"Quantity error for 'key': {e}")
    except TypeError:
        print(f"Error: key {key} must be a string.")


if __name__ == "__main__":
    print("=== Inventory System Analysis ===\n")
    inventory: dict[str, int] = dict()
    argv: list[str] = sys.argv
    for i in argv[1:]:
        if ":" not in i:
            print(f"Error - invalid parameter '{i}'")
            continue
        item: list[str] = i.split(":")
        key: str = str(item[0])
        try:
            if key in inventory:
                print(f"Redundant item '{key}' - discarding")
                continue
            value: int = int(item[1])
            inventory.update({key: value})
        except ValueError as e:
            print(f"Quantity error for 'key': {e}")
    print(f"Got inventory: {inventory}")
    total_items: int = 0
    for i in inventory.values():
        total_items = total_items + i
    unique_items: int = len(inventory)
    print(f"Total quantity of {unique_items} items: {total_items}")
    get_perc(inventory, total_items)
    get_stats(inventory)
    update_inventory("magic_item", 1, inventory)
