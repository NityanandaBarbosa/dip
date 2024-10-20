from usecases import *
from core import Paths

def main():
    rgb_to_grey = Resize()
    rgb_to_grey.execute(image_path= f'{Paths.INPUT}building.jpg')

if __name__ == "__main__":
    main()