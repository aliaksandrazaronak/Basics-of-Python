from dataclasses import dataclass
from tasks.Module_5.task_1 import Inventory, Item

import pyinputplus as pyip

LIGHT_WEIGHT_THRESHOLD = 40
HEAVY_WEIGHT_THRESHOLD = 50
MAX_WEIGHT_THRESHOLD = 60

MAP_ITEMS = [Item('gold coin', 6, 4), Item('bread', 3, 1), Item('rope', 2, 1), Item('arrow', 5, 8)]


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


@dataclass()
class Board:
    columns: int
    rows: int

    level = [
        ['X', '', 'X'],
        ['', 'X', ''],
        ['', 'X', ''],
    ]

    def print_board(self):
        for row in self.level:
            print(row)


board = Board(3, 3)
player = {'y': board.rows - 1, 'x': 0}
board.level[player['y']][player['x']] = 'H'

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
    board.print_board()
    move = input("Which direction?\n")

    if move.lower() == 'exit':
        break

    if not move_modifications.get(move):
        print("Invalid input")
        continue

    coordinates = move_modifications[move]

    new_y = player['y'] + coordinates['y']
    new_x = player['x'] + coordinates['x']

    if 0 <= new_y < board.rows and 0 <= new_x < board.columns:
        print(f"Hero moved {move}")

        board.level[player['y']][player['x']] = ''

        if board.level[new_y][new_x] == 'X':
            added_item = MAP_ITEMS.pop(0)
            hero_inventory.add_new_item_to_inventory(added_item)
            print("New item found!")
            print(f"It's a {added_item.name}")

        board.level[new_y][new_x] = 'H'

        player['y'] = new_y
        player['x'] = new_x

        hero_inventory.display_hero_inventory()
        stamina = hero.reduce_stamina()

        multiplier = hero_inventory.get_weight_multiplier()
        stamina *= multiplier
        print(f"Hero's stamina is equal {stamina}")
        print("========================")

        if stamina <= 0:
            if hero_inventory.inventory:
                print("Please drop any item!")
                response = pyip.inputYesNo(f"Do you want to drop any item?\n")
                if response == 'yes':
                    hero_inventory.drop_item_from_inventory()
                    continue

            print("Please eat something!")
            food_inventory_items = hero_inventory.get_food_items()
            if not food_inventory_items:
                board.print_board()
                print("Stamina is over! No any food! The End!")
                break
            for k in food_inventory_items:
                response = pyip.inputYesNo(f"Do you want to eat {k}?\n")
                if response == 'yes':
                    print(f"Hero has eaten {k}")
                    hero_inventory.inventory.pop(k)
                    hero.increase_stamina()
    else:
        print("Sorry, out of the board! Please choose correct direction")
