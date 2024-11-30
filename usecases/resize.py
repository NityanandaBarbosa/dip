import cv2
from core import ImageTransformer, Paths
from core.file_helper import FileHelper
from entities import File

class Resize(ImageTransformer):
    def __init__(self):
        pass
    
    @property
    def algorithm_name(self):
        return 'IMRESIZE'

    def execute(self, image_path : str):
        rgb_image = self._open_image(image_path=image_path)
        rgb_image_name = self._get_filename_and_type(path=image_path)
        resized_image = self._transform(rgb_image)
        self._save_image(file=rgb_image_name, image=resized_image)
        

    def _open_image(self, image_path : str):
        return FileHelper.open_image(image_path=image_path)

    def _transform(self, image):
        new_size = (300, 300)
        return cv2.resize(image, new_size)

    def _save_image(self, file : File, image : any):
        FileHelper.save_image(file=file, image=image, sufix='resized')

    def _get_filename_and_type(self, path : str) -> File:
       return FileHelper.get_filename_and_type(path=path)