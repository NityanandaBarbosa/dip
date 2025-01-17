import cv2
from core import ImageTransformer, Paths
from core.file_helper import FileHelper
from entities import File

class EdgeDectionCanny(ImageTransformer):
    def __init__(self):
        pass
    
    @property
    def algorithm_name(self):
        return 'CANNY_EDGE_DETECTION'

    def execute(self, image_path : str):
        rgb_image = self._open_image(image_path=image_path)
        rgb_image_name = self._get_filename_and_type(path=image_path)
        transformed_image = self._transform(rgb_image)
        self._save_image(file=rgb_image_name, image=transformed_image)
        

    def _open_image(self, image_path : str):
        return FileHelper.open_image(image_path=image_path)

    def _transform(self, image):
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray_image,100,200)
        return edges

    def _save_image(self, file : File, image : any):
        FileHelper.save_image(file=file, image=image, sufix= self.algorithm_name.lower())

    def _get_filename_and_type(self, path : str) -> File:
       return FileHelper.get_filename_and_type(path=path)