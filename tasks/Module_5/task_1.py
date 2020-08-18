from collections import defaultdict
from dataclasses import dataclass

import pyinputplus as pyip

LIGHT_WEIGHT_THRESHOLD = 60
HEAVY_WEIGHT_THRESHOLD = 70
MAX_WEIGHT_THRESHOLD = 80

UNWANTED_STUFF = ['rubbish', 'chewed gum', 'used tissue']

FOOD_ITEMS = ["meat", "egg", "bread"]


@dataclass
class Item:
    name: str
    weight: int
    price: int


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
        elif HEAVY_WEIGHT_THRESHOLD <= item_total < MAX_WEIGHT_THRESHOLD:
            print("\nCAUTION: Your equipment is very heavy, you're moving slower than usual!")
        elif item_total >= MAX_WEIGHT_THRESHOLD:
            print("\nCAUTION: You are overloaded, can't move!")
            print("Please eat something or drop some items to increase stamina!")

    def add_new_item_to_inventory(self, item):
        if item.name not in UNWANTED_STUFF:
            self.inventory[item.name] += item.weight
        return self.inventory

    def drop_item_from_inventory(self):
        item_name = pyip.inputMenu(list(self.inventory.keys()), numbered=True, blank=True)
        self.inventory.pop(item_name)
        print(f"{item_name} was dropped")
        return self.inventory

    def get_weight_multiplier(self):
        item_total = sum(self.inventory.values())
        if LIGHT_WEIGHT_THRESHOLD <= item_total < HEAVY_WEIGHT_THRESHOLD:
            return 0.9
        elif HEAVY_WEIGHT_THRESHOLD <= item_total < MAX_WEIGHT_THRESHOLD:
            return 0.8
        elif item_total >= MAX_WEIGHT_THRESHOLD:
            return 0
        return 1.1

    def food_items(self):
        return {k: v for k, v in self.inventory.items() if k in FOOD_ITEMS}


if __name__ == '__main__':
    inventory = Inventory()
    inventory.add_new_item_to_inventory(Item('gold coin', 3, 2))
    inventory.add_new_item_to_inventory(Item('gold coin', 43, 3))
    inventory.add_new_item_to_inventory(Item('rope', 2, 10))
    inventory.add_new_item_to_inventory(Item('torch', 4, 1))
    inventory.add_new_item_to_inventory(Item('torch', 2, 4))
    inventory.add_new_item_to_inventory(Item('dagger', 3, 8))
    inventory.add_new_item_to_inventory(Item('arrow', 7, 4))
    inventory.add_new_item_to_inventory(Item('arrow', 5, 9))
    inventory.display_hero_inventory()
