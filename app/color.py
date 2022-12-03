

import regex



class Color:
    def __init__(self, r: float, g: float, b: float):
        self.r = float(r)
        self.g = float(g)
        self.b = float(b)
    
    @staticmethod
    def from_hex(shex: str):
        match = regex.match(r"([0-9a-fA-F]{2})([0-9a-fA-F]{2})([0-9a-fA-F]{2})", shex)
        if match is None:
            raise RuntimeError("Syntax error")
        r, g, b = list(map(lambda x: int(x, 16) / 255.0, match.groups()))
        return Color(r, g, b)
    def to_hex(self) -> str:
        return "{:0>2X}{:0>2X}{:0>2X}".format(*list(map(lambda x: int(x * 255.0), (self.r, self.g, self.r))))

    def mix(self, bg: "Color", value: float):
        return self * value + bg * (1 - value)

    def __add__(self, color: "Color"):
        return Color(self.r + color.r, self.g + color.g, self.b + color.b)
    def __sub__(self, color: "Color"):
        return Color(self.r - color.r, self.g - color.g, self.b - color.b)
    def __mul__(self, value: float):
        return Color(self.r * value, self.g * value, self.b * value)
    def __div__(self, value: float):
        return Color(self.r / value, self.g / value, self.b / value)
    
    def __repr__(self) -> str:
        return "Color(#{})".format(self.to_hex())



