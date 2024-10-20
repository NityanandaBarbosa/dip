import cv2
from core import ImageTransformer, Paths
from entities import File

class RgbToGray(ImageTransformer):
    def __init__(self):
        pass
    
    @property
    def algorithm_name(self):
        return 'RGB2GRAY'

    def execute(self, image_path : str):
        rgb_image = self._open_image(image_path=image_path)
        rgb_image_name = self._get_rgb_filename_and_type(path=image_path)
        image_gray = self._transform(rgb_image)
        self._save_image(file=rgb_image_name, image=image_gray)
        

    def _open_image(self, image_path : str):
        image = cv2.imread(image_path)
        if image is None:
            print("Erro: não foi possível carregar a imagem. Verifique o caminho.")
            return Exception('Image not found')
        return image

    def _transform(self, image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    def _save_image(self, file : File, image : any):
        output_path = f'{Paths.OUTPUT}gray_{file.name_and_type}'
        cv2.imwrite(output_path, image)

    def _get_rgb_filename_and_type(self, path : str) -> File:
        filename = path.split('/')[-1].split('.')
        return File(filename[0], filename[-1])