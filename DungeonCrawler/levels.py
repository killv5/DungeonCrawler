from enemy import *
from barrier import *
from player import *

#end behavior goes left, up, right, up
def room1(data):
    data.roomCleared = False
    data.enemies = [Enemy(data.width*3//4, 120), Shotgun(data.width*4/5, 10), MachineGunEnemy(data.width*2/3, data.height*4/5)]
    data.barriers = [Barrier(data.width//2, 0, data.width//2, data.height*3//5, data.width, data.height)]
    data.endBehavior = ["Store", 2, "", ""]
    data.player.changePosition(data.width//2, data.height-100)

def room2(data):
    data.roomCleared = False
    data.enemies = [BigEnemy1(data.width//4, data.height//2)]
    data.barriers = []
    data.endBehavior = ["Store", "", "", 1]
    data.player.changePosition(data.width//2, data.height-100)