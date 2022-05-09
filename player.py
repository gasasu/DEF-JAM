import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Player:
    def __init__(self):
        self.location = None
        self.items = []
        self.inven = {}
        self.health = 50
        self.max_health = 50
        self.alive = True
        self.max_inventory = 5
        self.hasarmor = False
    # goes in specified direction if possible, returns True
    # if not possible returns False
    def now(self):
        clear()
        print()
        print(f"Your current health is {self.health}")
        print(f"{self.location.desc}")
        print(f"You have {len(self.items)} items in your inventory")
        print()
        input("Press enter to continue...")
    def goDirection(self, direction):
        new_location = self.location.getDestination(direction.lower())
        if new_location is not None:
            self.location = new_location
            return True
        return False
    def drop(self, item):
        item = item.lower()
        for i in self.items:
            if item == i.name.lower():
                self.items.remove(i)
                self.location.addItem(i)
                i.loc = self.location
                if self.inven[i.name] > 1:
                    self.inven[i.name] -=1
                else:
                    del self.inven[i.name]
                break
        else:
            print()
            print("No such item in inventory")
            print()
            input("Press enter to continue...")
    def pickup(self, item):
        if len(self.items) > self.max_inventory:
            print("You cannot add any more items. Consider dropping some items")
            print()
        else:
            self.items.append(item)
            item.loc = self
            self.location.removeItem(item)
            if item.name in self.inven:
                self.inven[item.name] += 1
            else:
                self.inven[item.name] = 1
    def showInventory(self):
        clear()
        print("You are currently carrying:")
        print()
        for item,value in self.inven.items():
            if value>1:
                print(f"{item} x{value}")
            else:
                print(f"{item}")
        print()
        input("Press enter to continue...")
    def attackMonster(self, mon):
        clear()
        print("You are attacking " + mon.name)
        print()
        print("Your health is " + str(self.health) + ".")
        print(mon.name + "'s health is " + str(mon.health) + ".")
        print()
        if self.health > mon.health:
            self.health -= mon.health
            print("You win. Your health is now " + str(self.health) + ".")
            mon.die()
        else:
            print("You lose.")
            self.alive = False
        print()
        input("Press enter to continue...")

    def inspect(self, item):
        item = item.lower()
        for i in self.items:
            if item == i.name.lower():
                clear()
                print(i.desc)
                print()
                input("Press enter to continue...")
                break
        else:
            for i in self.location.items:
                if item == i.name.lower():
                    clear()
                    print(i.desc)
                    print()
                    input("Press enter to continue...")
                    break
            else:
                clear()
                print("No such items in your inventory or in the room")
                print()
                input("Press enter to continue...")
    def kill(self, monster):
        for i in self.location.monsters:
            if monster.lower() == i.name.lower():
                i.die()
                return True

        else:
            clear()
            print("There is no such monster in the room")
            print()
            input("Press enter to continue...")
            return False
    def use(self, item):
        for i in self.items:
            if item.lower() == i.name.lower():
                self.items.remove(i)
                i.use(self)
                i.loc = None
                if self.inven[i.name] > 1:
                    self.inven[i.name] -=1
                else:
                    del self.inven[i.name]
                break
        else:
            print()
            print("No such item in inventory")
            print()
            input("Press enter to continue...")
    def getHit(self, weapon):
        if self.hasarmor:
            self.health -= 0.5 * weapon.powerpunch
        else:
            self.health -= weapon.powerpunch

    def show_weapons(self):
        count = 0
        print()
        print("These are the weapons you have in your inventory")
        print()
        for i in self.items:
            if i.isweapon:
                print()
                print(i.name)
                print()
                count += 1
        if count:
            return True
        else:
            print("None")
            print("\n Please go back and pick a weapon")
            input("Press enter to continue...")
            return False
    def getweapon(self, weapon):
        weapon = weapon.lower()
        for i in self.items:
            if weapon == i.name.lower():
                self.items.remove(i)
                i.loc = None
                if self.inven[i.name] > 1:
                    self.inven[i.name] -=1
                else:
                    del self.inven[i.name]
                return i
        else:
            print()
            print("No such weapon in your inventory")
            print()
            input("Press enter to continue...")
