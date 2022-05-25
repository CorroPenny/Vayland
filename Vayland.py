from time import sleep
import os
import datetime


if not os.path.exists("C:\\Temp"):
    os.makedirs("C:\\Temp")

now = datetime.datetime.now()

log = open("C:\\Temp\\VaylandLog" + now.strftime("%m-%d    %H-%M-%S") + ".txt", "a")

log.write("\nNew Game!\n\n")

print(now.strftime("%Y-%m-%d %H:%M:%S"))


print("Starting")


smallTown = "Vayland"
costOfGoods = 0
goldInBank = 100
sold = 0
bought = 0
amount = 0
mistyLove = 0



class Item:

    def __init__(self, name, value, weight, damage, protection):

        self.name = name
        self.value = value
        self.weight = weight
        self.damage = damage
        self.protection = protection

Sword = Item("Sword", 10, 2, 2, 0)
Axe = Item("Axe", 12, 3, 3, 0)
Dagger = Item("Dagger", 8, 1, 1, 0)
Plate = Item("Plate Armor", 20, 3, 0, 3)
Chain = Item("Chain Armor", 18, 2, 0, 2)
Leather = Item("Leather Armor", 16, 1, 0, 1)
Pick = Item("Pick", 5, 2, 0, 0)
MessKit = Item("MessKit", 6, 2, 0, 0)
Rope = Item("Rope", 4, 1, 0, 0)


inventory = [Plate, Pick, Sword, Sword, Chain, Plate]

log.write("Initiated Item Class, Items, and Inventory\n")








def TheForge():
    startForge = input("Welcome to the Forge! Here you may purchase or sell any of your tools or supplies.\nWhat would you like to do?\n\
Buy, Sell, Balance, Chat.\n").lower()
    global costOfGoods
    global smallTown
    global goldInBank
    global inventory
    global mistyLove
    # BUY
    log.write("Initiated Forge\n")
    if startForge == "buy":
        wantBuy = input("Wonderful! We offer many wares here. Would you like to see our Weapons, Armor, or Tools?\n").lower()
        print("You currently have " + str(goldInBank) + " Gold.")
        log.write("Forge Buy\n")

        # ARMOR PURCHASE
        if wantBuy == "armor":
            print("Of course! We have the best armor in town!\n")
            log.write("Armor Buy\n")

            def BuyArmor():
                global costOfGoods
                global sold
                global inventory

                armorBuy = input("Our Plate Armor is 20 Gold, Chainmaille Armor is 16 Gold, and Leather Armor is 12 Gold. Which would you like?\n").lower()

                if armorBuy == "plate" or armorBuy == "plate armor":
                    print("Plate Armor it is! I'll take your gold, thank ye very much!\n")
                    costOfGoods = Plate.value
                    ChargeGold(Plate.value)

                    if sold == 1:
                        inventory.append(Plate)
                    log.write("Purchase Plate\n")
                    TheForge()
            
                elif armorBuy == "chainmaille armor" or armorBuy == "chainmaille" or armorBuy == "chain":
                    print("Chainmaille Armor it is! I'll take your gold, thank ye very much!\n")
                    costOfGoods = Chain.value
                    ChargeGold(Chain.value)

                    if sold == 1:
                        inventory.append(Chain)
                    log.write("Purchase Chain\n")
                    TheForge()
            
                elif armorBuy == "leather armor" or armorBuy == "leather":
                    print("Leather Armor it is! I'll take your gold, thank ye very much!\n")
                    costOfGoods = Leather.value
                    ChargeGold(Leather.value)

                    if sold == 1:
                        inventory.append(Leather)
                    log.write("Purchase leather\n")
                    TheForge()

                elif armorBuy == "exit":
                    log.write("Exited Armor Purchase\n")
                    TheForge()
            
                else:
                    print("I'm not sure what you mean. Which would you like to purchase?")
                    BuyArmor()

            BuyArmor()

        # WEAPONS PURCHASE

        if wantBuy == "weapons" or wantBuy == "weapon":
            print("Of course! We have the best weapons in town!")

            def BuyWeapon():
                global costOfGoods
                global inventory
                global sold

                weaponBuy = input("Our Swords are 10 Gold, Axes are 12 Gold, and Daggers are 8 Gold. Which would you like to purchase?\n").lower()

                if weaponBuy == "sword" or weaponBuy == "swords":
                    print("A Sword it is! I'll take your gold, thank ye very much!\n")
                    costOfGoods = Sword.value
                    ChargeGold(Sword.value)

                    if sold == 1:
                        inventory.append(Sword)
                    TheForge()
            
                elif weaponBuy == "axe" or weaponBuy == "axes":
                    print("An Axe it is! I'll take your gold, thank ye very much!\n")
                    costOfGoods = Axe.value
                    ChargeGold(Axe.value)

                    if sold == 1:
                        inventory.append(Axe)
                    TheForge()

                elif weaponBuy == "dagger" or weaponBuy == "daggers":
                    print("A Dagger it is! I'll take your gold, thank ye very much!\n")
                    costOfGoods = Dagger.value
                    ChargeGold(Dagger.value)

                    if sold == 1:
                        inventory.append(Dagger)
                    TheForge()

                elif weaponBuy == "exit":
                    TheForge()

                else:
                    print("I'm not sure what you mean. Which would you like to purchase?")
                    BuyWeapon()

            BuyWeapon()

        # TOOLS PURCHASE

        if wantBuy == "tools" or wantBuy == "tool":

            def BuyTool():
                global costOfGoods

                toolBuy = input("Ah, a Worker I see!\nOur Picks are 10 Gold, Mess Kits are 12 Gold, and Ropes are 8 Gold. Which would you like to purchase?\n").lower()

                if toolBuy == "pick" or toolBuy == "picks":
                    print("A Pick it is! I'll take your gold, thank ye very much!\n")
                    costOfGoods = Pick.value
                    ChargeGold(Pick.value)

                    if sold == 1:
                        inventory.append(Pick)
                    TheForge()
            
                elif toolBuy == "mess kit":
                    print("A Mess Kit it is! I'll take your gold, thank ye very much!\n")
                    costOfGoods = MessKit.value
                    ChargeGold(MessKit.value)

                    if sold == 1:
                        inventory.append(MessKit)
                    TheForge()

                elif toolBuy == "rope" or toolBuy == "ropes":
                    print("A Rope it is! I'll take your gold, thank ye very much!\n")
                    costOfGoods = Rope.value
                    ChargeGold(Rope.value)

                    if sold == 1:
                        inventory.append(Rope)
                    TheForge()

                elif toolBuy == "exit":
                    TheForge()
            
                else:
                    print("I'm not sure what you mean. Which would you like to purchase?")
                    BuyTool()
            BuyTool()

        else:
            print("I'm not sure what you mean.\n")
            TheForge()


    # SELL
    elif startForge == "sell":
        SellAtForge()


    # Balance
    elif startForge == "balance":
        print("\nYou currently have: " + str(goldInBank) + " Gold\n")
        sleep(1)
        TheForge()



    # Chat
    elif startForge == "chat":
        wantChat = input("Ho there, traveller! My name be Misty. I'd love to tell you a bit about my Forge!\n\
1. What do you do here?\n\
2. What can I do for some Gold?\n\
3. How hot is your fire? <3\n").lower()

        if wantChat == "1":
            input("It is my passion to forge Armor, Weapons, and Tools! All of which I have for sale, and I am willing to purchase from you.\
Is there anything else you'd like to know?\n").lower()
        
        elif wantChat == "2":
            input("There is a bounty board outside of town! That's the only other way to earn gold here, unless you want to stay for a while...\n")

        elif wantChat == "3":
            input("I suppose that depends on how nice dinner is, stranger. But I'm sure it would impress you.\n")
            mistyLove = mistyLove + 1


        TheForge()



    elif startForge == "exit":
        GameStart()

    else:
        print("I'm not sure what you mean.\n")
        TheForge()


def TownHall():
    print("Loading Town Hall...")
    sleep(1)
    whatDoing = input("Welcome to Town Hall!")

    # Talk to mayor (requires social credit), take person to jail, talk to sherrif



    GameStart()


def TheTavern():
    print("Loading the Tavern...")
    sleep(1)
    input("Welcome to The Tavern!")

    # Buy drinks, buy food, talk to barkeep, talk to stranger (quest?)
     


    GameStart()


def TheInn():
    print("Loading the Inn...")
    sleep(1)
    input("Welcome to The Inn!")

    # Buy a room, talk to Innkeeper, store stuff?



    GameStart()


def ChargeGold(x):
    global goldInBank
    global costOfGoods
    global sold
    if goldInBank - x < 0:
        print("I'm sorry, you can't afford that.")
        sold = 0
    else:
        print("Starting Gold: " + str(goldInBank))
        goldInBank = goldInBank - x
        print("Charged " + str(x) + " Gold")
        log.write("Charged " + str(x) + " Gold\n")
        print("Remaining Gold: " + str(goldInBank) + "\n")
        log.write("Charged " + str(x) + " Gold\n")
        sold = 1
        sleep(1)

    
def SellItem(item):
    global goldInBank
    global costOfGoods
    global sold
    global bought
    global amount

    if amount > 0:
        inventory.remove(item)
        print("Sold " + item + "\n")
        log.write("Sold " + item + "\n")
        amount = amount - 1
        bought = bought + 1
        sleep(1)


def SellAtForge():
    global amount
    global goldInBank
    global costOfGoods
    global sold
    global bought

    print("Wonderful! I am willing to purchase any of your wares! What would you like to sell me?\nYou have these items available to sell...\n")
    for x in inventory:
        print(x.name)
    wantSell = input("")

    if wantSell == "exit":
        TheForge()
    
    else:
        count = 0
        for x in inventory:
            if wantSell == x.name:
                count = count + 1
        print(str(count) + " available for sale.")

        amount = input("How many of them would you like to sell?\n")

        if amount == "exit":
            SellAtForge()

        elif int(amount) > count:
            print("You only have " + str(count) + " available.\n")
            SellAtForge()

        else:
            while int(amount) > 0:
                for x in inventory:
                    if wantSell == x.name and int(amount) > 0:
                        inventory.remove(x)
                        print("Sold " + x.name)
                        log.write("Sold " + x.name + "\n")
                        print("+" + str(x.value) + " Gold")
                        log.write("+" + str(x.value) + " Gold\n")
                        amount = int(amount) - 1
                        bought = bought + 1
                        goldInBank = goldInBank + x.value
                        print("Balance: " + str(goldInBank) + " Gold\n")
                        log.write("Balance: " + str(goldInBank) + " Gold\n")
                        sleep(1)


    TheForge()


def ListInventory():
    
    for x in inventory:
        print(x.name)


def GameStart():
    sleep(1)
    goSomewhere = input("Where would you like to begin?\nThere are many establishments here in " + smallTown + ", such as... \n\
the Forge, Town Hall, the Tavern, and the Inn.\n").lower()
    if goSomewhere == "Forge" or goSomewhere == "forge" or goSomewhere == "The Forge" or goSomewhere == "the forge":
        print("To the Forge it is!")
        print("Loading the Forge...")
        sleep(1)
        TheForge()
    elif goSomewhere == "town hall" or goSomewhere == "Town Hall" or goSomewhere == "Town hall" or goSomewhere == "town Hall":
        print("To Town Hall it is!")
        TownHall()
    elif goSomewhere == "tavern" or goSomewhere == "Tavern" or goSomewhere == "the Tavern" or goSomewhere == "The tavern" or goSomewhere == "The Tavern" or goSomewhere == "the tavern":
        print("To the Tavern it is!")
        TheTavern()
    elif goSomewhere == "the Inn" or goSomewhere == "Inn" or goSomewhere == "The Inn" or goSomewhere == "the inn":
        print("To the Inn it is!")
        TheInn()
    else:
        print("I'm not sure what you mean. Would you mind trying again?")
        GameStart()


def RunIt():
    text = input("Are you ready?\nYes or No\n").lower()
    if text == "yes" or text == "Yes":
        print("Welcome to the game...")
        GameStart()
    else:
        print("Feel free to look around, we'll be ready when you are...\n")
        RunIt()










RunIt()