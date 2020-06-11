from collections import defaultdict

stuff = {'rope': 2, 'torch': 6, 'gold coin': 42, 'dagger': 3, 'arrow': 12}

dragonLoot = [
    'gold coin', 'chewed gum', 'dagger', 'used tissue', 'gold coin', 'chewed gum', 'torch',
    'gold coin', 'rubbish', 'used tissue', 'chewed gum', 'dagger', 'used tissue']

unused_stuff = ['rubbish', 'chewed gum', 'used tissue']

LIGHT_WEIGHT_THRESHOLD = 60
HEAVY_WEIGHT_THRESHOLD = 70
MAX_WEIGHT_THRESHOLD = 80

def display_inventory(inventory):
    print('\n'"Inventory:")
    for item_name, item_count in inventory.items():
        print(f"{item_count} {item_name}")

    item_total = sum(stuff.values())
    print('\n'f"Total number of items: {item_total}")
    if LIGHT_WEIGHT_THRESHOLD < item_total < HEAVY_WEIGHT_THRESHOLD:
        print('\n'"CAUTION: Your backpack weighs a lot, your stamina runs out quicker!")
    elif HEAVY_WEIGHT_THRESHOLD < item_total < MAX_WEIGHT_THRESHOLD:
        print('\n'"CAUTION: Your equipment is very heavy, you're moving slower than usual!")
    elif item_total >= MAX_WEIGHT_THRESHOLD:
        print('\n'"CAUTION: You are overloaded, can't move!")

def add_to_inventory(inventory, added_items):
    skipped = defaultdict(int)
    number_of_new_added_items = 0

    for new_item in added_items:
        if new_item in unused_stuff:
            skipped[new_item] += 1
        else:
            inventory[new_item] += 1
            number_of_new_added_items +=1

    print(f"Added {number_of_new_added_items} items to inventory")
    print(f"Skipped:")
    for item_name, item_count in skipped.items():
        print(f"{item_count} {item_name}")
    return inventory

new_inventory = add_to_inventory(stuff, dragonLoot)
display_inventory(new_inventory)
