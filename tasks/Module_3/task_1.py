from collections import defaultdict

import pyinputplus as pyip
import random

ingredients_and_prices = defaultdict()

bread_type = pyip.inputMenu(['wheat', 'white', 'sourdough'], numbered=True)
bread_price = round(random.uniform(3.5, 7), 2)
ingredients_and_prices[bread_type] = bread_price

protein_type = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], numbered=True)
protein_price = round(random.uniform(2, 4.5), 2)
ingredients_and_prices[protein_type] = protein_price

prompt = 'Do you want a cheese?\n'
response = pyip.inputYesNo(prompt)
if response == 'yes':
    cheese_type = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'], numbered=True)
    cheese_price = round(random.uniform(5, 8.5), 2)
    ingredients_and_prices[cheese_type] = cheese_price

prompt = 'Do you want a sauce type?\n'
response = pyip.inputYesNo(prompt)
if response == 'yes':
    sauce_type = pyip.inputMenu(['mayo', 'mustard', 'lettuce', 'tomato'], numbered=True)
    sauce_price = round(random.uniform(6.5, 7.5), 2)
    ingredients_and_prices[sauce_type] = sauce_price

prompt = 'How many sandwiches do you want to buy?\n'
sandwiches_count = pyip.inputNum(prompt, min=1)

total_ingredients_price = sum(ingredients_and_prices.values())

print("Your sandwich consists of " + ', '.join(ingredients_and_prices.keys()) + ".")
print(f"You want to buy {sandwiches_count} sandwich(es)")
print(f"That's a total of {sandwiches_count * total_ingredients_price} eur")


