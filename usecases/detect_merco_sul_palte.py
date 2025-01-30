import cv2
from core import ImageTransformer, Paths
from core.file_helper import FileHelper
from entities import File

class DetectMercoSulPlate(ImageTransformer):
    def __init__(self):
        pass
    
    @property
    def algorithm_name(self):
        return 'DETECT_MERCO_SUL_PLATE'

    def execute(self, image_path : str):
        rgb_image = self._open_image(image_path=image_path)
        rgb_image_name = self._get_filename_and_type(path=image_path)
        transformed_image = self._transform(rgb_image)
        self._save_image(file=rgb_image_name, image=transformed_image)
        
    def _open_image(self, image_path : str):
        return FileHelper.open_image(image_path=image_path)

    def _transform(self, image):
        placa_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_russian_plate_number.xml")
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        placas = placa_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
        if len(placas) > 0:
            text = "Placa identificada"
            color = (0, 255, 0)  # Verde
        else:
            text = "Nenhuma placa identificada"
            color = (0, 0, 255)  # Vermelho
        
        cv2.putText(image, text, (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2, cv2.LINE_AA)
        return image

    def _save_image(self, file : File, image : any):
        FileHelper.save_image(file=file, image=image, sufix= self.algorithm_name.lower())

    def _get_filename_and_type(self, path : str) -> File:
        return FileHelper.get_filename_and_type(path=path)
