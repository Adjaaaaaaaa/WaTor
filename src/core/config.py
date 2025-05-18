#PARAM MONDE

CELL_SIZE = 25
WIDTH = 20
HEIGHT = 20
#PARAM POPULATION
NB_TUNA: int = 150
NB_SHARK: int = 40

#PARAM REPRODUCTION
TUNA_REPRODUCTION_TIME: int = 6
SHARK_REPRODUCTION_TIME: int = 12

#PARAM ENERGY
SHARK_INITIAL_ENERGY: int = 10
SHARK_ENERGY_GAIN: int = 7

# Path
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TUNA_IMAGE_PATH = os.path.join(BASE_DIR, "..", "..", "assets", "tuna.png")
SHARK_IMAGE_PATH = os.path.join(BASE_DIR, "..", "..", "assets", "shark.png")