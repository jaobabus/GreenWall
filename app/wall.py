

from .console import Console
from .color import Color
from .map import Map, Size
import random
import time


SPEED_CONSTANT = 10
LIGHT_CONSTANT = 0.1
FADE_CONSTANT = 0.01

default_wall_alphabet = "0123456789qwertyuiop[]asdfghjkl;'zxcvbnm,./!@#$%^&*()_~`=+-QWERTYUIOP{}\\|ASDFGHJKL:\"ZXCVBNM<>?"


class WallEntity:
    def __init__(self, position: "tuple(int, int)", color: Color,
                 speed: float = 1.0, light: float = 1.0):
        self.position = Size(*position)
        self.color = color
        self.speed = speed
        self.light = light
        self.alive = True



class Wall:
    def __init__(self, map_size: "tuple(int, int)", bg_color: Color = Color(0, 0, 0)):
        self._map = Map(*map_size)
        self._entities: list[WallEntity] = []
        self.backgroud = bg_color
        
        self._last_entities_len = 0
        self._last_frame_time = time.time()
        self._fps = 0
        for y in range(0, self._map.size()[1]):
            Console.str_set_pos(0, y)
            print(' ' * self._map.size().x)
        print("Entities {:>3}  FPS {:>2}".format(100, 10))

    def summon(self, pos: "tuple(int, int)", color: Color, speed: float = 1.0, light: float = 1.0) -> bool:
        x, y = int(pos[0]), int(pos[1])
        if self._map[x, y] and self._map[x, y][1] > 0.1 or pos[1] < 2:
            return False
        self._entities.append(WallEntity(pos, color, speed, light))
        return True
        
    def do(self, elapsed: float = 1 / 60) -> None:
        for entity in self._entities:
            entity.position.y += entity.speed * elapsed * SPEED_CONSTANT
            entity.light -= entity.speed * elapsed * LIGHT_CONSTANT
            if entity.position[0] > self._map.size()[0] or entity.position[1] > self._map.size()[1] or entity.light <= 0:
                entity.alive = False
        self._entities = [entity for entity in self._entities if entity.alive]
    
    def redraw(self, alphabet = default_wall_alphabet, elapsed: float = 1 /60) -> None:        
        for entity in self._entities:
            x, y = int(entity.position.x), int(entity.position.y)
            self._map[x, y] = [entity.color, entity.light]

        line = ""
        for y in range(0, self._map.size()[1]):
            for x in range(self._map.size()[0]):
                cell = self._map[x, y] or [Color(0, 0, 0), 0.0]
                if cell[1] > 0.0:
                    cell[1] -= FADE_CONSTANT
                    line += (Console.str_set_pos(x, y) + 
                             Console.str_set_color(cell[0].mix(self.backgroud, cell[1])) + 
                             (random.choice(alphabet) if cell[1] > 0.0 else " "))
        print(line, end='')

        self._fps = (1 / (time.time() - self._last_frame_time)) * 0.7 + self._fps * 0.3
        self._last_frame_time = time.time()
        Console.set_pos(0, 0)   
        Console.set_color(Color(0.8, 0.4, 0.0))
        print("Entities {:>3}  FPS {:>2}".format(len(self._entities), int(self._fps)))
        self._last_entities_len = len(self._entities)
