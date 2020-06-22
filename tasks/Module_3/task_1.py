from collections import defaultdict

import pyinputplus as pyip

ingredients_and_prices = defaultdict()

bread_price = {"wheat": 1.5, "white": 0.8, "sourdough": 2.1}
meat_price = {"chicken": 5, "turkey": 3.2, "ham": 4.1, "tofu": 5.5}
cheese_price = {"cheddar": 3.1, "swiss": 2.5, "mozzarella": 1.9}
sauce_price = {"mayo": 0.7, "mustard": 0.2, "lettuce": 0.5, "tomato": 1.1}

bread_type = pyip.inputMenu(['wheat', 'white', 'sourdough'], numbered=True)
bread_type_price = bread_price.get(bread_type)
ingredients_and_prices[bread_type] = bread_type_price

meat_type = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], numbered=True)
meat_type_price = meat_price.get(meat_type)
ingredients_and_prices[meat_type] = meat_type_price

response = pyip.inputYesNo('Do you want a cheese?\n')
if response == 'yes':
    cheese_type = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'], numbered=True)
    cheese_type_price = cheese_price.get(cheese_type)
    ingredients_and_prices[cheese_type] = cheese_type_price

response = pyip.inputYesNo('Do you want a sauce type?\n')
if response == 'yes':
    sauce_type = pyip.inputMenu(['mayo', 'mustard', 'lettuce', 'tomato'], numbered=True)
    sauce_type_price = sauce_price.get(sauce_type)
    ingredients_and_prices[sauce_type] = sauce_type_price

sandwiches_count = pyip.inputNum('How many sandwiches do you want to buy?\n', min=1)

total_ingredients_price = sum(ingredients_and_prices.values())

print(f"Your sandwich consists of {', '.join(ingredients_and_prices.keys())}.")
print(f"You want to buy {sandwiches_count} sandwich(es)")
print(f"That's a total of {sandwiches_count * total_ingredients_price} eur")


