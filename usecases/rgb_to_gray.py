import cv2
from core.image_transformer import ImageTransformer
from entities.file import File

_ASSETS_PATH_OUTPUT = 'assets/output/'
class RgbToGray(ImageTransformer):
    def __init__(self):
        pass

    def execute(self, image_path : str):
        rgb_image = self._open_image(image_path=image_path)
        rgb_image_name = self._get_rgb_filename_and_type(path=image_path)
        image_gray = self._transform(rgb_image)
        self._save_image(file=rgb_image_name, image_gray=image_gray)
        

    def _open_image(self, image_path : str):
        image = cv2.imread(image_path)
        if image is None:
            print("Erro: não foi possível carregar a imagem. Verifique o caminho.")
            return Exception('Image not found')
        return image

    def _transform(self, rgb_image):
        return cv2.cvtColor(rgb_image, cv2.COLOR_BGR2GRAY)

    def _save_image(self, file : File, image_gray : any):
        output_path = f'{_ASSETS_PATH_OUTPUT}{file.name_and_type}'
        cv2.imwrite(output_path, image_gray)

    def _get_rgb_filename_and_type(self, path : str) -> File:
        filename = path.split('/')[-1].split('.')
        return File(filename[0], filename[-1])