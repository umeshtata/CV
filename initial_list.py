"""
Purpose: To add the initial list of items into database i.e., pickle file 
"""

import pickle

fin = open("files/list.pickle", "wb")

fried_rice = ["Fried Rice",[ {"Code" : 1, "Name": "Pineapple Fried Rice", "Cost" : 70}, {"Code" : 2, "Name": "Veg Fried Rice", "Cost" : 80},\
               {"Code" : 3, "Name": "Gobi Fried Rice", "Cost" : 90},{"Code" : 4, "Name": "Paneer Fried Rice", "Cost" : 100},\
                {"Code" : 5, "Name": "Egg Fried Rice", "Cost" : 120},{"Code" : 6, "Name": "Chicken Fried Rice", "Cost" : 130},\
                    {"Code" : 7, "Name": "Schezwan Gobi Fried Rice", "Cost" : 140},{"Code" : 8, "Name": "Schezwan Paneer Fried Rice", "Cost" : 150},\
                        {"Code" : 9, "Name": "Schezwan Egg Fried Rice", "Cost" : 160},{"Code" : 10, "Name": "Schezwan Chicken Fried Rice", "Cost" : 170}]]

noodles = ["Noodles" ,[{"Code" : 11, "Name": "Veg Noodles", "Cost" : 70}, {"Code" : 12, "Name": "Gobi Noodles", "Cost" : 80},\
               {"Code" : 13, "Name": "Paneer Noodles", "Cost" : 90},{"Code" : 14, "Name": "Egg Noodles", "Cost" : 100},\
                {"Code" : 15, "Name": "Chicken Noodles", "Cost" : 110},{"Code" : 16, "Name": "Schezwan Egg Noodles", "Cost" : 120},\
                    {"Code" : 17, "Name": "Schezwan Paneer Noodles", "Cost" : 140},{"Code" : 18, "Name": "Schezwan Gobi Noodles", "Cost" : 150},\
                        {"Code" : 19, "Name": "Schezwan Chicken Noodles", "Cost" : 160},{"Code" : 20, "Name": "Shrimp Noodles", "Cost" : 170}]]

drinks = ["Drinks" , [{"Code" : 21, "Name": "Water Bottle", "Cost" : 20}, {"Code" : 22, "Name": "Thumps Up", "Cost" : 30},\
               {"Code" : 23, "Name": "Pepsi", "Cost" : 30},{"Code" : 24, "Name": "Coco Cola", "Cost" : 30},\
                {"Code" : 25, "Name": "Sprite", "Cost" : 30},{"Code" : 26, "Name": "Friut Drink", "Cost" : 20},\
                    {"Code" : 27, "Name": "Tea", "Cost" : 15},{"Code" : 28, "Name": "Milk", "Cost" : 10},\
                        {"Code" : 29, "Name": "Coffee", "Cost" : 15},{"Code" : 30, "Name": "Milkshake",  "Cost" : 40}]]

extras = ["Extras",[{"Code" : 31, "Name": "Vada", "Cost" : 20}, {"Code" : 32, "Name": "Samosa", "Cost" : 15},\
               {"Code" : 33, "Name": "French fries", "Cost" : 25},{"Code" : 34, "Name": "Bajji", "Cost" : 15},\
                {"Code" : 35, "Name": "Sandwich", "Cost" : 20},{"Code" : 36, "Name": "Omlete", "Cost" : 15},\
                    {"Code" : 37, "Name": "Cutlet", "Cost" : 20},{"Code" : 38, "Name": "Veg Puff", "Cost" : 15},\
                        {"Code" : 39, "Name": "Egg Puff", "Cost" : 20},{"Code" : 40, "Name": "Chicken Puff",  "Cost" : 25}]]
    
pickle.dump(fried_rice, fin)
pickle.dump(noodles, fin)
pickle.dump(drinks, fin)
pickle.dump(extras, fin)
