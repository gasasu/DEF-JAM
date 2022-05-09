import random
import updater

class Monster:
    def __init__(self, name, health, room, weapon):
        self.name = name
        self.health = health
        self.room = room
        self.weapon = weapon
        room.addMonster(self)
        updater.register(self)
    def update(self):
        #if random.random() < .5:
            #self.moveTo(self.room.randomNeighbor())
        pass
    def moveTo(self, room):
        self.room.removeMonster(self)
        self.room = room
        room.addMonster(self)
    def die(self):
        self.room.removeMonster(self)
        updater.deregister(self)
    def getHit(self, weapon):
        self.health -= weapon.powerpunch
