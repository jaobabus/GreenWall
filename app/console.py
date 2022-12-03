

from .color import Color
import colorama


COLOR_DBG = False

colorama.init()



class Console:
    current_color = Color(0, 0, 0)
    current_style = []
    __styles_stack = []
    
    @staticmethod
    def get_size() -> (int, int):
        raise NotImplementedError("Not console API")
    @staticmethod
    def resize(x: int, y: int) -> None:
        raise NotImplementedError("Resize not supported")

    @staticmethod    
    def get_pos(x: int, y: int, size: int) -> str:
        raise NotImplementedError("Not console API")
    @staticmethod
    def set_pos(x: int, y: int) -> None:
        Console.__send_style([y, x], 'H')
    @staticmethod
    def str_set_pos(x: int, y: int) -> str:
        return Console.__get_str_style([y, x], 'H')

    @staticmethod    
    def __get_str_style(seq: list[str], term: str = 'm') -> None:
        return "\033[{}{}".format(';'.join(map(str, seq)), term)
    @staticmethod    
    def __send_style(seq: list[str], term: str = 'm') -> None:
        if COLOR_DBG:
            print("\\e[{}{}".format(';'.join(map(str, seq)), term))
        else:
            print(Console.__get_str_style(seq, term))
    @staticmethod
    def __apply_style(style: bool = True, color: bool = True) -> None:
        if Console.current_style or Console.current_color:
            if Console.current_style and style:
                Console.__send_style(Console.current_style or [0], 'm')
            if Console.current_color and color:
                color = Console.current_color
                Console.__send_style([38, 2, int(color.r * 255.0), int(color.g * 255.0), int(color.b * 255.0)], 'm')
        else:
            Console.reset_color()

    @staticmethod        
    def set_color(color: Color) -> None:
        Console.current_color = color
        Console.__apply_style(False, True)
    @staticmethod        
    def str_set_color(color: Color) -> str:
        return Console.__get_str_style([38, 2, int(color.r * 255.0), int(color.g * 255.0), int(color.b * 255.0)], 'm')
    @staticmethod
    def set_style(bold: bool = False, faded: bool = False, italic: bool = False, 
                  underlined: bool = False, flashing: bool = False, strikethrough: bool = False) -> None:
        Console.current_style = []
        if bold:          Console.current_style.append('1')
        if faded:         Console.current_style.append('2')
        if italic:        Console.current_style.append('3')
        if underlined:    Console.current_style.append('4')
        if flashing:      Console.current_style.append('5')
        if strikethrough: Console.current_style.append('9')
        Console.__apply_style(True, False)
    @staticmethod
    def reset_color() -> None:
        Console.__send_style([0], 'm')
        Console.current_color = Color(0, 0, 0)
        Console.current_style = []
    @staticmethod
    def push_color() -> None:
        Console.__styles_stack.append((Console.current_color, Console.current_style))
    @staticmethod
    def pop_color() -> None:
        Console.current_color, Console.current_style = Console.__styles_stack.pop(-1)
        Console.__apply_style(True, True)
    





