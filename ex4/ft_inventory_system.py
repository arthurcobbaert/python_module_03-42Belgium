import sys

def get_perc(inventory: dict[str, int], total: int) -> None:
		perc: float = 0
		for key, value in inventory.items():
			perc = value * 100 / total
			if value == 1:
				print(f"{key}: {value} unit ({perc:.1f}%)")
			else:
				print(f"{key}: {value} units ({perc:.1f}%)")
def get_stats(inventory: dict[str, int]) -> None:
		most: int = 0
		most_key: str = ""
		least: int = 0;
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
		if most == 1:
			print(f"Most abundant: {most_key} ({most} unit)")
		else:
			print(f"Most abundant: {most_key} ({most} units)")
		if least == 1:
			print(f"Least abundant: {least_key} ({least} unit)")
		else:
			print(f"Least abundant: {least_key} ({least} units)")
def get_categorie(inventory: dict[str, int]) -> None:
		scarce: dict[str, int] = {}
		moderate: dict[str, int] = {}
		abundant: dict[str, int] = {}
		for key, value in inventory.items():
			if 0 <= value < 5:
				scarce.update({key: value})
			elif value <= 7:
				moderate.update({key: value})
			else:
				abundant.update({key: value})
		if len(abundant) > 0:
			print(f"Abundant: {abundant}")
		if len(moderate) > 0:
			print(f"Moderate: {moderate}")
		if len(scarce) > 0:
			print(f"Scarce: {scarce}")
def get_suggestions(inventory: dict[str, int]) -> None:
	restock: dict[str, int] = {}
	for key, value in inventory.items():
		if value == 1:
			restock.update({key:value})
	print(f"Restock needed:", end=" ")
	first: bool = True
	for key in restock.keys():
		if not first:
			print(",", end=" ")
		first = False
		print(key, end="")
	print("\n")
def get_properties(inventory: dict[str, int]) -> None:
	first_key: bool = True
	first_value: bool = True
	print("Dictionary keys:", end=" ")
	for key in inventory.keys():
		if not first_key:
			print(",", end=" ")
		print(key, end="")
		first_key = False
	print("\nDictionary values:", end=" ")
	for value in inventory.values():
		if not first_value:
			print(",", end=" ")
		first_value = False
		print(value, end="")
	print("\nSample lookup - 'sword' in inventory:", "sword" in inventory.keys())
if __name__ == "__main__":
	print("=== Inventory System Analysis ===")
	inventory: dict[str, int] = dict()
	argv: list[str] = sys.argv
	for i in argv[1:]:
		item: list[str] = i.split(":")
		key: str = item[0]
		value: int = int(item[1])
		inventory.update({key: value})
	total_items: int = 0
	for i in inventory.values():
		total_items = total_items + i
	unique_items: int = len(inventory)
	print(f"Total items in inventory: {total_items}")
	print(f"Unique item types: {unique_items}\n")
	print("=== Current inventory ===")
	get_perc(inventory, total_items)
	print("\n=== Inventory Statistics ===")
	get_stats(inventory)
	print("\n=== Item Categories ===")
	get_categorie(inventory)
	print("\n=== Management Suggestions ===")
	get_suggestions(inventory)
	print("=== Dictionary Properties Demo ===")
	get_properties(inventory)
