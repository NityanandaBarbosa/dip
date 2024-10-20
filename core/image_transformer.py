
from abc import ABC, abstractmethod
from entities.file import File

class ImageTransformer(ABC):
    @property
    @abstractmethod
    def algorithm_name(self):
        pass

    @abstractmethod
    def execute(self, image_path: str):
        """Método principal para executar a transformação de imagem."""
        pass

    @abstractmethod
    def _open_image(self, image_path: str):
        """Abre a imagem a partir de um caminho."""
        pass

    @abstractmethod
    def _transform(self, image):
        """Aplica a transformação na imagem."""
        pass

    @abstractmethod
    def _save_image(self, file: File, image: any):
        """Salva a imagem transformada."""
        pass

    @abstractmethod
    def _get_rgb_filename_and_type(self, path: str) -> File:
        """Obtém o nome e a extensão do arquivo."""
        pass