
import cv2

from core.paths import Paths
from entities.file import File


class FileHelper:
    @staticmethod
    def open_image(image_path : str):
        image = cv2.imread(image_path)
        if image is None:
            print("Erro: não foi possível carregar a imagem. Verifique o caminho.")
            raise Exception('Image not found')
        return image
        
    @staticmethod
    def save_image(file : File, image : any, sufix : str) -> list[str]:
        output_path = f'{Paths.OUTPUT}{sufix}_{file.name_and_type}'
        print(f'\nImagem transformada salva em {output_path}\n')
        cv2.imwrite(output_path, image)
    
    @staticmethod
    def get_filename_and_type(path : str) -> File:
        filename = path.split('/')[-1].split('.')
        return File(filename[0], filename[-1])
