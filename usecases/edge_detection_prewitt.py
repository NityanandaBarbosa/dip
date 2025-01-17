import cv2
import numpy as np
from core import ImageTransformer, Paths
from core.file_helper import FileHelper
from entities import File

class EdgeDetectionPrewitt(ImageTransformer):
    def __init__(self):
        pass
    
    @property
    def algorithm_name(self):
        return 'PREWITT_EDGE_DETECTION'

    def execute(self, image_path: str):
        rgb_image = self._open_image(image_path=image_path)
        rgb_image_name = self._get_filename_and_type(path=image_path)
        transformed_image = self._transform(rgb_image)
        self._save_image(file=rgb_image_name, image=transformed_image)

    def _open_image(self, image_path: str):
        return FileHelper.open_image(image_path=image_path)

    def _transform(self, image):
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        kernel_x = np.array([[-1, 0, 1], 
                             [-1, 0, 1], 
                             [-1, 0, 1]])
        kernel_y = np.array([[-1, -1, -1], 
                             [ 0,  0,  0], 
                             [ 1,  1,  1]])
        grad_x = cv2.filter2D(gray_image, -1, kernel_x)
        grad_y = cv2.filter2D(gray_image, -1, kernel_y)
        edges = cv2.addWeighted(grad_x, 0.5, grad_y, 0.5, 0)
        return edges

    def _save_image(self, file: File, image: any):
        FileHelper.save_image(file=file, image=image, sufix=self.algorithm_name.lower())

    def _get_filename_and_type(self, path: str) -> File:
        return FileHelper.get_filename_and_type(path=path)
