from usecases.rgb_to_gray import RgbToGray

INPUT_FOLDER = 'assets/input/'

if __name__ == "__main__":
    rgb_to_grey = RgbToGray()
    rgb_to_grey.execute(image_path= f'{INPUT_FOLDER}building.jpg')