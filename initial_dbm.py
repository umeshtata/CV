"""
Purpose: Creating the initial dbm file to store the count of each item
"""
import dbm

file = "files/item_order"
dbo = dbm.open(file, 'c')

# Adding the Fried Rices
dbo['Pineapple Fried Rice'] = '0'
dbo['Veg Fried Rice'] = '0'
dbo['Gobi Fried Rice'] = '0'
dbo['Paneer Fried Rice'] = '0'
dbo['Egg Fried Rice'] = '0'
dbo['Chicken Fried Rice'] = '0'
dbo['Schezwan Gobi Fried Rice'] = '0'
dbo['Schezwan Paneer Fried Rice'] = '0'
dbo['Schezwan Egg Fried Rice'] = '0'
dbo['Schezwan Chicken Fried Rice'] = '0'

# Adding the Noodles
dbo['Veg Noodles'] = '0'
dbo['Gobi Noodles'] = '0'
dbo['Paneer Noodles'] = '0'
dbo['Egg Noodles'] = '0'
dbo['Chicken Noodles'] = '0'
dbo['Schezwan Gobi Noodles'] = '0'
dbo['Schezwan Paneer Noodles'] = '0'
dbo['Schezwan Egg Noodles'] = '0'
dbo['Schezwan Chicken Noodles'] = '0'
dbo['Shrimp Noodles'] = '0'

# Inserting the Drinks
dbo['Water Bottle'] = '0'
dbo['Thumps Up'] = '0'
dbo['Pepsi'] = '0'
dbo['Coco Cola'] = '0'
dbo['Sprite'] = '0'
dbo['Fruit Drink'] = '0'
dbo['Tea'] = '0'
dbo['Milk'] = '0'
dbo['Coffee'] = '0'
dbo['Milkshake'] = '0'

# Inserting the Extras
dbo['Vada'] = '0'
dbo['Samosa'] = '0'
dbo['French fries'] = '0'
dbo['Bajji'] = '0'
dbo['Sandwich'] = '0'
dbo['Omlete'] = '0'
dbo['Cutlet'] = '0'
dbo['Veg Puff'] = '0'
dbo['Egg Puff'] = '0'
dbo['Chicken Puff'] = '0'