

from .console import Console, Color
from .wall import Wall, WallEntity
import time
import random



def run(bg_color: Color):
    wall = Wall((80, 24))
    
    while True:
        wall.summon((random.randint(0, 80), random.randint(0, 24)), Color(0, 1, 0), 
                    random.randint(30, 100) / 100)
        wall.do()
        if wall._fps > 60:
            time.sleep(1 / 80)
        wall.redraw()

