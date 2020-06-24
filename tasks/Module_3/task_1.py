import pyinputplus as pyip

composed_sandwich = {}

BREAD_PRICE = {"wheat": 1.5, "white": 0.8, "sourdough": 2.1}
MEAT_PRICE = {"chicken": 5, "turkey": 3.2, "ham": 4.1, "tofu": 5.5}
CHEESE_PRICE = {"cheddar": 3.1, "swiss": 2.5, "mozzarella": 1.9}
SAUCE_PRICE = {"mayo": 0.7, "mustard": 0.2, "lettuce": 0.5, "tomato": 1.1}

bread_type = pyip.inputMenu(list(BREAD_PRICE.keys()), numbered=True)
composed_sandwich[bread_type] = BREAD_PRICE[bread_type]

meat_type = pyip.inputMenu(list(MEAT_PRICE.keys()), numbered=True)
composed_sandwich[meat_type] = MEAT_PRICE[meat_type]

response = pyip.inputYesNo('Do you want a cheese?\n')
if response == 'yes':
    cheese_type = pyip.inputMenu(list(CHEESE_PRICE.keys()), numbered=True)
    composed_sandwich[cheese_type] = CHEESE_PRICE[cheese_type]

response = pyip.inputYesNo('Do you want a sauce type?\n')
if response == 'yes':
    sauce_type = pyip.inputMenu(list(SAUCE_PRICE.keys()), numbered=True)
    composed_sandwich[sauce_type] = SAUCE_PRICE[sauce_type]

sandwiches_count = pyip.inputNum('How many sandwiches do you want to buy?\n', min=1)

total_ingredients_price = sum(composed_sandwich.values())

print(f"Your sandwich consists of {', '.join(composed_sandwich.keys())}.")
print(f"You want to buy {sandwiches_count} sandwich(es)")
print(f"That's a total of {sandwiches_count * total_ingredients_price} eur")
