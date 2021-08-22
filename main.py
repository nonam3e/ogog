import sys
import time
from game_of_life import GameofLife

WIDTH = 1920
HEIGHT = 1080

conway = GameofLife(scale=20)
fps = 16

while True:
    try:
        conway.run()
        time.sleep(0.2)
    except KeyboardInterrupt:
        sys.exit(0)