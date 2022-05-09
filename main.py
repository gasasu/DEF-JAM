from room import Room
from player import Player
from item import Item, Health, Sword, Handgun, AK47, Armor
from monster import Monster
import os
import updater
import random

player = Player()

#def createWorld():
#   pass
room1 = Room("This is your first room",1)
room2 = Room("Get some free stuff",2)
room3 = Room("Get some more free stuff maybe",3)
room4 = Room("Meet monster 1",4)
room5 = Room("Opens when you defeat monster 1",5)
room6 = Room("Meet monster 2",6)
room7 = Room("Opens when you defeat monster 2, Get some other free stuff",7)
room8 = Room("You meet monster 3",8)
Room.connectRooms(room1, "north", room2, "south")
Room.connectRooms(room2, "east", room3, "west")
Room.connectRooms(room3, "north", room4, "south")
#Room.connectRooms(d, "east", e, "west")
Room.connectRooms(room5, "north", room6, "south")
#Room.connectRooms(g, "west", f, "east")
Room.connectRooms(room7, "north", room8, "south")
#i = Item("Rock", "This is just a rock.")
#i.putInRoom(b)
#j = Item("Rock", "This is just a rock.")
#j.putInRoom(a)

sword = Sword()
sword.putInRoom(room2)
player.location = room1
a = Sword()
b = Handgun()
c = AK47()
Monster("FAT JOE", 20, room4,a)
Monster("Rick Ross", 50, room6,b)
Monster("Snoop Dogg", 100, room8,c)

def free_gift(room):
    free_gift = random.randint(1,2)
    a = Sword()
    b = Handgun()
    c = AK47()
    d = Health()
    e = Armor()
    gifts = [a,b,c,d,e]
    random.shuffle(gifts)
    while free_gift:
        gift = gifts[random.randint(0,len(gifts)-1)]
        gift.putInRoom(room)
        free_gift -= 1
    return

free_gift(room5)
free_gift(room7)
free_gift(room3)
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
# so fights are going to be you choose a weeapon
#  a weapon can be used for only one fight
# you can use your armor at anytime before you begin to fight
#once fight commences, only ends when one person wins
# if you lose, your're dead and you have to start the quest again

def attack(player, weapon, monster):
    clear()
    print()
    print(f"You begin your fight against {monster.name}")
    print(f"Your current health is {player.health}")
    print(f"{monster.name}'s current health is {monster.health}")
    print("Remember, you die when your health reaches Zero")
    print()
    input("Press enter to continue...")
    while True:
        clear()
        print(f"Your current health is {player.health}")
        print(f"{monster.name}'s current health is {monster.health}")
        print()
        print("Which direction do you want to fire? Left or Right")
        print()
        player_dir = input("Direction: ")
        monster_dir = random.randint(0,1)
        if player_dir.lower() == "right":
            if monster_dir:
                monster.getHit(weapon)
                print()
                print("You landed your shot")
                input("Press enter to continue...")
            else:
                print()
                print("You missed your shot")
                input("Press enter to continue...")
        else:
            if not monster_dir:
                monster.getHit(weapon)
                print()
                print("You landed your shot")
                input("Press enter to continue...")
            else:
                print()
                print("You missed your shot")
                input("Press enter to continue...")
        if player.health <= 0:
            player.alive = False
            clear()
            print("You failed your quest")
            print("This shouldn't be the end")
            print("Better luck next time")

            return
        if monster.health <= 0:
            monster.die()
            return

        clear()
        print(f"Your current health is {player.health}")
        print(f"{monster.name}'s current health is {monster.health}")
        print()
        print(f"Now {monster.name} gets to fire at you")
        print()
        print("Which direction do you want to move to? Left or Right")
        print()
        player_dir = input("Direction? ")
        monster_dir = random.randint(0,1)
        if monster_dir:
            if player_dir.lower() == "right":
                player.getHit(monster.weapon)
                print()
                print(f"{monster.name} landed his shot")
                input("Press enter to continue...")
            else:
                print()
                print(f"{monster.name} missed his shot")
                input("Press enter to continue...")
        else:
            if player_dir.lower() == "left":
                player.getHit(monster.weapon)
                print()
                print(f"{monster.name} landed his shot")
                input("Press enter to continue...")
            else:
                print()
                print(f"{monster.name} missed his shot")
                input("Press enter to continue...")
        if player.health <= 0:
            player.alive = False
            clear()
            print("You failed your quest")
            print("This shouldn't be the end")
            print("Better luck next time")
            return
        if monster.health <= 0:
            monster.die()
            return





flag1,flag2,flag3,flag4,flag5, flag6, flag7, flag8 = True, True, True, True, True, True, True, True

def printSituation():
    global flag1, flag2, flag3, flag4, flag5, flag6, flag7, flag8
    if player.location.id == 8 and flag8:
        if not player.location.hasMonsters():
            clear()
            print("Congratulations you have completed this quest")
            print("You have your hands on the emerald")
            print("Be sure to donate some of your proceeding from the emerald to the game designers")
            print("Till we meet next time")
            print()
            input("Press enter to continue...")
            return True
    if player.location.id == 6 and flag6:
        if not player.location.hasMonsters():
            clear()
            print("Congratulations you have defeated your second monster in this quest")
            print("You have unlocked the door to ")
            print("You have uncovered some new items")
            print("You have earned five additional health points")
            input("Press enter to continue...")
            Room.connectRooms(room7, "west", room6, "east")
            free_gift(player.location)
            player.max_health += 5
            player.hasarmor = False
            flag6 = False
    if player.location.id == 7 and flag7:
        if not player.location.hasMonsters():
            clear()
            print("Welcome to the Hospital")
            print("Facing off with snoop Dogg can be a very challenging task and we want you to feel supported.")
            print("Therefore we are gifting you a free health boost to give you a fighting chance")
            print()
            input("Press enter to continue...")
            player.health = player.max_health
            flag7 = False
    if player.location.id == 4 and flag4:
        clear()
        print()
        print("In this room you meet the first monster")
        print("Use any gifts or weapons in your inventory")
        print("You can choose to attack the monster anytime you are ready")
        print("You can go south back into room3")
        print()
        input("Press enter to continue...")
        if not player.location.hasMonsters():
            clear()
            print("Congratulations you have defeated your first monster")
            print("You have unlocked the door")
            print("You have uncovered some new items")
            print("You have earned five additional health points")
            input("Press enter to continue...")
            Room.connectRooms(room4, "east", room5, "west")
            free_gift(player.location)
            player.max_health += 5
            player.hasarmor = False
            flag4 = False
    if player.location.id == 1 and flag1:
        clear()
        print()
        print("This is where you begin your quest")
        print("You can go north to enter the next room")
        input("Press enter to continue...")
        flag1 = False
    if player.location.id == 2 and flag2:
        clear()
        print()
        print("Welcome to the second room")
        print("There is a sword provided to you to battle any monsters you may encounter")
        print("Be sure to pickup the sword as you won't be able to fight a monster without a weapon")
        print()
        input("Press enter to continue...")
        flag2 = False
    if player.location.id == 3 and flag3:
        clear()
        print()
        print("This is a randomly generated room")
        print("You might find some free gifts in this room")
        print("Be sure to inspect them before picking up to ascertain if you would need them")
        print("You can go west back into room 2")
        print("You can go north into room4")
        print()
        input("Press enter to continue...")
        flag3 = False
    if player.location.id == 5 and flag5:
        clear()
        print()
        print("This is a randomly generated room")
        print("You might find some free gifts in this room")
        print("Be sure to inspect them before picking up to ascertain if you would need them")
        print("You can go west back into room 4")
        print("You can go north into room 6")
        print()
        input("Press enter to continue...")
        flag5 = False


    clear()
    print(player.location.desc)
    print()
    if player.location.hasMonsters():
        print("This room contains the following monsters:")
        for m in player.location.monsters:
            print(m.name)
        print()
    if player.location.hasItems():
        print("This room contains the following items:")
        for i in player.location.items:
            print(i.name)
        print()
    print("You can go in the following directions:")
    for e in player.location.exitNames():
        print(e)
    print()

def showHelp():
    clear()
    print("go <direction> -- moves you in the given direction")
    print("inventory -- opens your inventory")
    print("inspect <item>-- provides a description of the item")
    print("pickup <item> -- picks up the item")
    print("drop <item> -- drops off the item")
    print("Attack <monster> -- attacks a monster")
    print("me -- shows your current status")
    print("use <item>-- to use a one time item")
    print("wait -- Time passes in the game")
    print("quit -- quits the game")
    print()
    input("Press enter to continue...")


#createWorld()
def introduction():
    clear()
    print("WELCOME TO THE BORING GAME")
    print("In this uneventful game you are going on a quest")
    print("The goal of the quest is to steal an emerald protected by some monsters.")
    print("This emerald is worth billions on the market")
    print()
    print("To get the emerald you need to go through a series of rooms, each containing either a monster or some free gifts")
    print("Your goal is to defeat the monsters using the gifts you get")
    print("These gifts are randomly assigned and may include weapons to fight monsters")
    print("You would need to be tactical in using which gift at what time since all gifts can be used just once")
    print("Goodluck on your quest!!")
    print()
    print()
    print("This game is inspired by the game DEF JAM")
    print("All characters in the game are fictional, any likeness to actual people is purely coincidental")
    input("Press enter to continue...")

introduction()
playing = True
while playing and player.alive:
    if printSituation():
         break
    commandSuccess = False
    timePasses = False
    while not commandSuccess:
        commandSuccess = True
        command = input("What now? ")
        commandWords = command.split()
        if commandWords[0].lower() == "go":   #cannot handle multi-word directions
            okay = player.goDirection(commandWords[1])
            if okay:
                timePasses = True
            else:
                print("You can't go that way.")
                commandSuccess = False
        elif commandWords[0].lower() == "pickup":  #can handle multi-word objects
            targetName = command[7:] # everything after "pickup "
            target = player.location.getItemByName(targetName)
            if target != False:
                player.pickup(target)
            else:
                print("No such item.")
                commandSuccess = False

        elif commandWords[0].lower() == "inventory":
            player.showInventory()

        elif commandWords[0].lower() == "help":
            showHelp()

        elif commandWords[0].lower() == "quit":
            playing = False

        elif commandWords[0].lower() == "attack":
            targetName = command[7:]
            target = player.location.getMonsterByName(targetName)
            if target != False:
                #player.attackMonster(target)
                if player.show_weapons():
                    print()
                    print("Please select a weapon to use.  ")
                    weapon = input("Weapon? ")
                    weapon = player.getweapon(weapon)
                    if weapon:
                        attack(player, weapon, target)
                else:
                    commandSuccess = False

            else:
                print("No such monster.")
                commandSuccess = False

        elif commandWords[0].lower() == "drop":
            drop_item = command[5:]
            player.drop(drop_item)

        elif commandWords[0].lower() == "inspect":
            ins_name = command[8:]
            player.inspect(ins_name)

        elif commandWords[0].lower() == "wait":
            timePasses = True

        elif commandWords[0].lower() == "me":
            player.now()

        elif commandWords[0].lower() == "kill":
            mons = command[5:]
            player.kill(mons)

        elif commandWords[0].lower() == "use":
            he = command[4:]
            player.use(he)


        else:
            print("Not a valid command")
            commandSuccess = False
    if timePasses == True:
        updater.updateAll()
