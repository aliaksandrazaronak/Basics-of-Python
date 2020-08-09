from collections import defaultdict
from dataclasses import dataclass

import pyinputplus as pyip

LIGHT_WEIGHT_THRESHOLD = 40
HEAVY_WEIGHT_THRESHOLD = 50
MAX_WEIGHT_THRESHOLD = 60

unwanted_stuff = ['rubbish', 'chewed gum', 'used tissue']


@dataclass
class Item:
    name: str
    weight: int
    price: int


class Food(Item):
    def __init__(self, name, attitude, price):
        super().__init__(name, attitude, price)


map_items = [Item('gold coin', 6, 4), Food('bread', 3, 1), Item('rope', 2, 1), Item('arrow', 5, 8)]
food_items = ["meat", "egg", "bread"]


class Inventory:

    def __init__(self):
        self.inventory = defaultdict(int)

    def display_hero_inventory(self):
        print("\nInventory:")
        for item_name, item_count in self.inventory.items():
            print(f"{item_count} {item_name}")

        item_total = sum(self.inventory.values())
        print(f"Total number of items: {item_total}")
        if LIGHT_WEIGHT_THRESHOLD <= item_total < HEAVY_WEIGHT_THRESHOLD:
            print("\nCAUTION: Your backpack weighs a lot, your stamina runs out quicker!")
            return 0.9
        elif HEAVY_WEIGHT_THRESHOLD <= item_total < MAX_WEIGHT_THRESHOLD:
            print("\nCAUTION: Your equipment is very heavy, you're moving slower than usual!")
            return 0.8
        elif item_total >= MAX_WEIGHT_THRESHOLD:
            print("\nCAUTION: You are overloaded, can't move!")
            print("Please eat something or drop some items to increase stamina!")
            return 0
        return 1.1

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
            self.stamina -= 10
        return self.stamina

    def increase_stamina(self):
        self.stamina += 10
        print(f"Stamina was increased to {self.stamina}")
        return self.stamina


@dataclass
class Board:
    columns: int
    rows: int


level = [
    ['X', '', 'X'],
    ['', 'X', ''],
    ['', 'X', ''],
]


def print_board():
    for row in level:
        print(row)


board = Board(3, 3)
player = {'y': board.rows - 1, 'x': 0}
level[player['y']][player['x']] = 'H'

move_modifications = {'north': {'y': -1, 'x': 0},
                      'south': {'y': 1, 'x': 0},
                      'west': {'y': 0, 'x': -1},
                      'east': {'y': 0, 'x': 1}}

hero_inventory = Inventory()
hero_inventory.add_new_item_to_inventory(Item('gold coin', 43, 3))
hero_inventory.add_new_item_to_inventory(Item('rope', 2, 10))
hero_inventory.add_new_item_to_inventory(Item('arrow', 5, 4))
hero_inventory.add_new_item_to_inventory(Item('egg', 5, 4))
hero = Hero()

# Main game loop
while True:
    print_board()
    move = input("Which direction?\n")
    print(f"Hero moved {move}")

    if move.lower() == 'exit':
        break

    if not move_modifications.get(move):
        print("Invalid input")
        continue

    coords = move_modifications[move]

    new_y = player['y'] + coords['y']
    new_x = player['x'] + coords['x']

    if 0 <= new_y < board.rows and 0 <= new_x < board.columns:

        level[player['y']][player['x']] = ''

        if level[new_y][new_x] == 'X':
            added_item = map_items.pop(0)
            hero_inventory.add_new_item_to_inventory(added_item)
            print("New item found!")
            print(f"It's a {added_item.name}")

        level[new_y][new_x] = 'H'

        player['y'] = new_y
        player['x'] = new_x

        multiplier = hero_inventory.display_hero_inventory()

        stamina = hero.reduce_stamina()
        stamina *= multiplier
        print(f"Hero's stamina is equal {stamina}")
        print("========================")

        if stamina <= 0:
            food_inventory_items = {k: v for k, v in hero_inventory.inventory.items() if k in food_items}
            if len(food_inventory_items) == 0:
                print_board()
                print("Stamina is over! No any food! The End!")
                break
            for k in food_inventory_items:
                response = pyip.inputYesNo(f"Do you want to eat {k}?\n")
                if response == 'yes':
                    print(f"Hero has eaten {k}")
                    hero_inventory.inventory.pop(k)
                    hero.increase_stamina()
    else:
        print("Oops, out of the board")
