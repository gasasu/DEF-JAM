import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
items = ['Health', 'Armor', 'Sword', 'Handgun', 'AK47']
class Item:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.loc = None
    def describe(self):
        clear()
        print(self.desc)
        print()
        input("Press enter to continue...")
    def putInRoom(self, room):
        self.loc = room
        room.addItem(self)


class Sword(Item):
    def __init__(self):
        self.name = "sword"
        self.desc = "a sword for fighting monsters"
        self.loc = None
        self.powerpunch = 5
        self.isweapon = True

class Handgun(Item):
    def __init__(self):
        self.name = "Handgun"
        self.desc = "a hand gun for fighting monsters"
        self.loc = None
        self.powerpunch = 10
        self.isweapon = True

class AK47(Item):
    def __init__(self):
        self.name = "AK47"
        self.desc = "an AK47 for fighting monsters"
        self.loc = None
        self.powerpunch = 15
        self.isweapon = True

class Health(Item):
    def __init__(self):
        self.name = "Health"
        self.desc = "Replenishes health"
        self.loc = None
        self.isweapon = False

    def use(self,player):
        player.health = player.max_health

class Armor(Item):
    def __init__(self):
        self.name = "Armor"
        self.desc = "Helps defend against enemies, Can be used only once in a fight"
        self.loc = None
        self.isweapon = False
    def use(self, player):
        player.hasarmor = True
