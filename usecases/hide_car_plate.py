import cv2
from core import ImageTransformer, Paths
from core.file_helper import FileHelper
from entities import File

class HideCarPlate(ImageTransformer):
    def __init__(self):
        pass
    
    @property
    def algorithm_name(self):
        return 'HIDE_CAR_PLATE'

    def execute(self, image_path : str):
        rgb_image = self._open_image(image_path=image_path)
        rgb_image_name = self._get_filename_and_type(path=image_path)
        transformed_image = self._transform(rgb_image)
        self._save_image(file=rgb_image_name, image=transformed_image)
        

    def _open_image(self, image_path : str):
        return FileHelper.open_image(image_path=image_path)

    def _transform(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        edged = cv2.Canny(blur, 30, 150)
        contours, _ = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for c in contours:
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.02 * peri, True)
            if len(approx) == 4:
                x, y, w, h = cv2.boundingRect(approx)
                aspect_ratio = w / h if h != 0 else 0 
                if 3.2 < aspect_ratio < 3.5:
                    print(aspect_ratio)
                    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 0), -1)

        return image



    def _save_image(self, file : File, image : any):
        FileHelper.save_image(file=file, image=image, sufix= 'hide_plate')

    def _get_filename_and_type(self, path : str) -> File:
       return FileHelper.get_filename_and_type(path=path)