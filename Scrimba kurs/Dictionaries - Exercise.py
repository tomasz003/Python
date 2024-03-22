swords_shop = {"name": "Swords Shop", "purchases": 0, "wooden sword": 80, "copper sword": 120, "steel sword": 140, "silver sword": 200 }
shields_shop = {"name": "Shields Shop", "purchases": 0, "wooden shield": 20, "copper shield": 30, "steel shield": 35, "silver shield": 50}
armor_shop = {"name": "Armor Shop", "purchases": 0, "helmet": 20, "gantlet": 5, "chainmail": 15}

equipment = []
money = 210


def buy_one(shop):
    global money
    if shop["purchases"]==0:
        item=input(f"What do you want to buy in {shop['name']}?\n")
        if item=="exit":
            print("Goodbye!")
        elif item in shop and item!="name" and item!="purchases" and shop[item]<=money:
            cost=shop.pop(item)
            equipment.append(item)
            money-=cost
            shop["purchases"]+=1
            print(f"You've just bought {item}!\nYou have {money} money left.")
        elif (item in shop and item!="name" and item!="purchases"):
            print(f"Failed to purchase - you need {shop[item]} money for it (you have {money} money).")
        else:
            print(f"There is no {item} in {shop['name']}")
    else:
        print(f"You cannot buy more items in {shop['name']}!")     


print(f"Hello Adventurer!\n\nYou need to arm yourself before the germanic tribe reaches the village! Good luck!\nYou have {money} money.")
while((buying:=(input("\nDo you want to buy another item? (yes or no)\n"))).lower()=="yes" and len(equipment)<3):
        
    wanted=input("What do you want to buy? Sword, shield or armor?\n")
    if wanted == "sword":
        print("Swords shop has wooden sword, copper sword, steel sword and silver sword. Type \"exit\" to leave swords shop.")
        buy_one(swords_shop)
    elif wanted == "shield":
        print("Shields shop has wooden shield, copper shield, steel shield and silver shield. Type \"exit\" to leave shields shop.")
        buy_one(shields_shop)
    elif wanted == "armor":
        print("Armor shop has helmet, gantlet and chainmail. Type \"exit\" to leave armor shop.")
        buy_one(armor_shop)
    else: 
        print("Wrong object. Try again.")
    print(f"Equipment: {', '.join(equipment)}.")

if buying=="no":
    print(f"\nYou've completed your equipment: {', '.join(equipment)}. Good luck fighting!")
else:
    print("\nI'll take it as a \"no\". Goodbye and good luck with figthing!")