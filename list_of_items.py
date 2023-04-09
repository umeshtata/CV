"""
Purpose: This code is made in the purpose of updation of items 
         either in the terms of change of price of an item or an addition of an item
"""
import pickle
import dbm

fr = open("files/list.pickle", "rb")                            # Opening pickle file to get the previous data

fried_rice = pickle.load(fr)
noodles = pickle.load(fr)
drinks = pickle.load(fr)
extras = pickle.load(fr)
fr.close()


def update_information(fried_rice, noodles, drinks, extras):    # Function for updation of data base  
    
    n = int(input("Enter number of items to be updated: "))
    
    for i in range(n):
        k = int(input("Enter\n1.Update Existing Item 2.Add New Item: "))
        
        if k == 1:                                              # Updating the price of an existing item
            d = int(input("Enter the category:\n1.Fried rice 2.Noodles 3.Drinks 4.Extras: "))
            
            if d == 1:
                fried_rice = ["Fried Rice"].append(update_cost(fried_rice))
            elif d == 2: 
                noodles = ["Noodles"].append(update_cost(noodles))
            elif d == 3: 
                drinks = ["Drinks"].append(update_cost(drinks))
            elif d == 4: 
                extras = ["Extras"].append(update_cost(extras))
            else:
                print("Incorrect Option")
        
        elif k == 2:                                            # Adding a new item              
            d = int(input("Enter the category:\n1.Fried rice 2.Noodles 3.Drinks 4.Extras: "))
            
            p = {}
            p["Code"] = int(input("Enter the Code: "))
            p["Name"] = input("Enter the Name: ")
            p["Cost"] = int(input("Enter the Cost: "))
            
            fin = dbm.open("files/item_order", "c")             # The new item must also be added in dbm file
            fin[p["Name"]] = "0"
            
            if d == 1:
                temp = fried_rice[1]
                temp.append(p)
                fried_rice = ["Fried Rice"].append(p)
            elif d == 2:
                temp = noodles[1]
                temp.append(p)
                noodles = ["Noodles"].append(p)
            elif d == 3: 
                temp = drinks[1]
                temp.append(p)
                drinks = ["Drinks"].append(p)
            elif d == 4: 
                temp = extras[1]
                temp.append(p)
                extras = ["Extras"].append(p)
            else:
                print("Incorrect option")
        
        else:
            print("Incorrect Option")

# Function which is used to update the item price
def update_cost(item_list):
    l = item_list[1]
    for i in l:
        print(i["Name"], end = ",")
    print()
    k = input("Choose the item name: ")
    c = int(input("Enter the updated cost: "))
    for i in l:
        if i["Name"] == k:
            i["Cost"] = c
    return l

# As an item to be added the whole data is re-written       
fin = open("files/list.pickle", "wb")
print(fried_rice)
print(noodles)
print(drinks)
print(extras)

update_information(fried_rice, noodles, drinks, extras)     # Calling the update function 

# Dumping back the new data
pickle.dump(fried_rice, fin)
pickle.dump(noodles, fin)
pickle.dump(drinks, fin)
pickle.dump(extras, fin)

fin.close()                                                 # Closing the file
 
print(fried_rice)
print(noodles)
print(drinks)
print(extras)