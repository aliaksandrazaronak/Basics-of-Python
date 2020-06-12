from collections import defaultdict

stuff = {'rope': 2, 'torch': 6, 'gold coin': 42, 'dagger': 3, 'arrow': 12}

dragon_loot = [
    'gold coin', 'chewed gum', 'dagger', 'used tissue', 'gold coin', 'chewed gum', 'torch',
    'gold coin', 'rubbish', 'used tissue', 'chewed gum', 'dagger', 'used tissue']

unwanted_stuff = ['rubbish', 'chewed gum', 'used tissue']

LIGHT_WEIGHT_THRESHOLD = 60
HEAVY_WEIGHT_THRESHOLD = 70
MAX_WEIGHT_THRESHOLD = 80

def display_inventory(inventory):
    print("\nInventory:")
    for item_name, item_count in inventory.items():
        print(f"{item_count} {item_name}")

    item_total = sum(inventory.values())
    print(f"\nTotal number of items: {item_total}")
    if LIGHT_WEIGHT_THRESHOLD < item_total < HEAVY_WEIGHT_THRESHOLD:
        print("\nCAUTION: Your backpack weighs a lot, your stamina runs out quicker!")
    elif HEAVY_WEIGHT_THRESHOLD < item_total < MAX_WEIGHT_THRESHOLD:
        print("\nCAUTION: Your equipment is very heavy, you're moving slower than usual!")
    elif item_total >= MAX_WEIGHT_THRESHOLD:
        print("\nCAUTION: You are overloaded, can't move!")

def add_to_inventory(inventory, added_items):
    skipped = defaultdict(int)
    added_items_count = 0

    for new_item in added_items:
        if new_item in unwanted_stuff:
            skipped[new_item] += 1
        else:
            inventory[new_item] += 1
            added_items_count +=1

    print(f"Added {added_items_count} items to inventory")
    print("Skipped:")
    for item_name, item_count in skipped.items():
        print(f"{item_count} {item_name}")
    return inventory

new_inventory = add_to_inventory(stuff, dragon_loot)
display_inventory(new_inventory)