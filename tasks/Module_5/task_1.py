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


class Inventory:
    dragon_loot = [
        Item('gold coin', 2, 4), Item('chewed gum', 1, 0), Item('dagger', 3, 1),
        Item('gold coin', 3, 1), Item('gold coin', 2, 1), Item('torch', 5, 10),
        Item('rubbish', 5, 0), Item('chewed gum', 1, 5), Item('used tissue', 1, 2)]

    def __init__(self):
        self.inventory = defaultdict(int)

    def display_hero_inventory(self, hero_inventory):
        print("\nInventory:")
        for item_name, item_count in hero_inventory.items():
            print(f"{item_count} {item_name}")

        item_total = sum(hero_inventory.values())
        print(f"\nTotal number of items: {item_total}")
        if LIGHT_WEIGHT_THRESHOLD < item_total < HEAVY_WEIGHT_THRESHOLD:
            print("\nCAUTION: Your backpack weighs a lot, your stamina runs out quicker!")
        elif HEAVY_WEIGHT_THRESHOLD < item_total < MAX_WEIGHT_THRESHOLD:
            print("\nCAUTION: Your equipment is very heavy, you're moving slower than usual!")
        elif item_total >= MAX_WEIGHT_THRESHOLD:
            print("\nCAUTION: You are overloaded, can't move!")

    def add_items_to_inventory_from_dragon_loot(self, dragon_loot_items):
        skipped = defaultdict(int)
        added_items_count = 0
        total_items_weight = 0

        for item in dragon_loot_items:
            if item.name in unwanted_stuff:
                skipped[item.name] += item.weight
            else:
                self.inventory[item.name] += item.weight
                added_items_count += 1
                total_items_weight += item.weight

        print(f"Added {added_items_count} items to inventory with total weight of items {total_items_weight}")
        print("Skipped:")
        for item_name, item_count in skipped.items():
            print(f"{item_count} {item_name}")
        return self.inventory

    def add_new_item_to_inventory(self, item):
        if item.name not in unwanted_stuff:
            self.inventory[item.name] += item.weight
        return self.inventory


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
    final_hero_inventory = inventory.add_items_to_inventory_from_dragon_loot(inventory.dragon_loot)
    inventory.display_hero_inventory(final_hero_inventory)
