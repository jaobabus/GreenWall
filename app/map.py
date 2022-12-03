


class Size:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        
    def __getitem__(self, index: int) -> int:
        return [self.x, self.y] [index] 

class Map:
    def __init__(self, x_size: int, y_size: int):
        self._size = Size(x_size, y_size)
        self._map = [None] * x_size * y_size
    
    def size(self) -> Size:
        return self._size

    def __getitem__(self, index: "tuple(int, int)") -> None:
        index = (index[0] + self._size[0]) % self._size[0], (index[1] + self._size[1]) % self._size[1]
        if index[0] >= self._size[0] or index[1] >= self._size[1]:
            raise ValueError("Out of range")
        return self._map[index[0] + index[1] * self._size[0]]
    
    def __setitem__(self, index: "tuple(int, int)", value: None) -> None:
        index = (index[0] + self._size[0]) % self._size[0], (index[1] + self._size[1]) % self._size[1]
        if index[0] >= self._size[0] or index[1] >= self._size[1]:
            raise ValueError("Out of range")
        self._map[index[0] + index[1] * self._size[0]] = value

