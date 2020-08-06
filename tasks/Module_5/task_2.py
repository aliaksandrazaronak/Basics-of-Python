from collections import defaultdict
from dataclasses import dataclass

LIGHT_WEIGHT_THRESHOLD = 60
HEAVY_WEIGHT_THRESHOLD = 70
MAX_WEIGHT_THRESHOLD = 80

unwanted_stuff = ['rubbish', 'chewed gum', 'used tissue']


@dataclass
class Item:
    name: str
    weight: int
    price: int


map_items = [Item('gold coin', 2, 4), Item('dagger', 3, 1), Item('gold coin', 2, 1), Item('dagger', 5, 8)]


class Inventory:

    def __init__(self):
        self.inventory = defaultdict(int)

    def display_hero_inventory(self):
        print("\nInventory:")
        for item_name, item_count in self.inventory.items():
            print(f"{item_count} {item_name}")

        item_total = sum(self.inventory.values())
        print(f"Total number of items: {item_total}")
        if LIGHT_WEIGHT_THRESHOLD < item_total < HEAVY_WEIGHT_THRESHOLD:
            print("\nCAUTION: Your backpack weighs a lot, your stamina runs out quicker!")
        elif HEAVY_WEIGHT_THRESHOLD < item_total < MAX_WEIGHT_THRESHOLD:
            print("\nCAUTION: Your equipment is very heavy, you're moving slower than usual!")
        elif item_total >= MAX_WEIGHT_THRESHOLD:
            print("\nCAUTION: You are overloaded, can't move!")

    def add_new_item_to_inventory(self, item):
        if item.name not in unwanted_stuff:
            self.inventory[item.name] += item.weight
        return self.inventory

    def drop_item_from_inventory(self):
        removed_item = self.inventory.popitem()
        print(f"{removed_item} was dropped")
        return self.inventory


class Hero:

    def __init__(self):
        self.stamina = 50

    def reduce_stamina(self):
        if self.stamina > 0:
            self.stamina -= 20
        return self.stamina


level = [
    ['X', '', 'X'],
    ['', 'X', ''],
    ['', 'X', ''],
]


def print_level():
    """ Print level row-wise so that it retains its 2D shape """
    for row in level:
        print(row)


# Object to store the player coords
player = {'y': 2, 'x': 0}
level[player['y']][player['x']] = 'H'
print_level()

# Translate keywords into coordinate changes
move_modifications = {'UP': {'y': -1, 'x': 0},
                      'DOWN': {'y': 1, 'x': 0},
                      'LEFT': {'y': 0, 'x': -1},
                      'RIGHT': {'y': 0, 'x': 1}}

inventory = Inventory()
inventory.add_new_item_to_inventory(Item('gold coin', 43, 3))
inventory.add_new_item_to_inventory(Item('rope', 2, 10))
hero = Hero()

# Main game loop
while True:
    print(f"Stamina = {hero.stamina}")
    move = input("Which direction?")

    # Give them the option to quit
    if move.lower() == 'exit':
        break

    if not move_modifications.get(move):
        print("Invalid input")
        continue

    coords = move_modifications[move]

    new_y = player['y'] + coords['y']
    new_x = player['x'] + coords['x']

    if 0 <= new_y < 3 and 0 <= new_x < 3:
        level[player['y']][player['x']] = ' '
        level[new_y][new_x] = 'H'

        # Update player coords
        player['y'] = new_y
        player['x'] = new_x

        # Show hero's inventory
        inventory.display_hero_inventory()

        # Reduce_stamina
        stamina = hero.reduce_stamina()
        if stamina <= 0:
            print("Stamina is over! The End!")
            break

        # Print result
        print("========================")
        print_level()
    else:
        print("Oops, out of the board")
