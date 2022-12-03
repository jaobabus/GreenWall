

from app.app import *
import sys



if __name__ == '__main__':
    bg = sys.argv[1] if len(sys.argv) > 1 else "000000"
    run(Color.from_hex(bg))



