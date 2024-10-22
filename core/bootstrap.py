import os
import platform
import importlib.util
import inspect
from time import sleep
from . import ImageTransformer, Paths

class Bootstrap:
    def _get_usecases(self) -> list[ImageTransformer]:
        transformers : list[ImageTransformer] = []
        for arquivo in os.listdir(Paths.USECASES):
            if arquivo.endswith('.py') and arquivo != '__init__.py':
                file_path = os.path.join(Paths.USECASES, arquivo)
                spec = importlib.util.spec_from_file_location(arquivo[:-3], file_path)
                modulo = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(modulo)

                for nome, obj in inspect.getmembers(modulo):
                    if inspect.isclass(obj) and issubclass(obj, ImageTransformer) and obj != ImageTransformer:
                        instancia = obj()
                        transformers.append(instancia)

        return transformers
    
    def _get_images(self) -> list[str]:
        images : list[str] = []
        self._clear_terminal()
        for image in os.listdir(Paths.INPUT):
            if not image.endswith('.py'):
               print(f'image {image}')
               images.append(image)

        return images
    
    def _choose_image(self, images : list[str]) -> str:
        print("Escolha um nome da lista:\n")
        for index, image in enumerate(images):
            print(f"{index+1}: {image}")
        print(f"{len(images)+1}: SAIR\n")
        while True:
            try:
                choice = int(input("Digite o índice do nome que deseja escolher: ")) - 1
                images_len = len(images)
                if 0 <= choice < images_len:
                    print(f"Você escolheu: {images[choice]}")
                    return images[choice]
                elif choice == images_len:
                    return
                else:
                    self._clear_terminal()
                    print("Índice inválido. Tente novamente.\n")
            except ValueError:
                self._clear_terminal()
                print("Por favor, digite um número válido.\n")
            sleep(1)
            self._clear_terminal()
            return self._choose_image(images= images)
    
    
    
    def _choose_usecase(self, usecases : list[ImageTransformer]) -> ImageTransformer:
        print("Escolha um nome da lista:\n")
        for index, usecase in enumerate(usecases):
            print(f"{index+1}: {usecase.algorithm_name}")
        print(f"{len(usecases)+1}: SAIR\n")
        while True:
            try:
                choice = int(input("Digite o índice do nome que deseja escolher: ")) - 1
                usecases_len = len(usecases)
                if 0 <= choice < usecases_len:
                    print(f"Você escolheu: {usecases[choice].algorithm_name}")
                    return usecases[choice]
                elif choice == usecases_len:
                    return
                else:
                    self._clear_terminal()
                    print("Índice inválido. Tente novamente.\n")
            except ValueError:
                self._clear_terminal()
                print("Por favor, digite um número válido.\n")
            sleep(1)
            self._clear_terminal()
            return self._choose_usecase(usecases= usecases)
    
    def _clear_terminal(self):
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")
        
    
    def execute(self):
        try:
            usecases = self._get_usecases()
            usecase = self._choose_usecase(usecases=usecases)
            if(usecase is not None):
                images = self._get_images()
                image = self._choose_image(images=images)
                usecase.execute(image_path=f'{Paths.INPUT}{image}')
        except Exception as e:
            print(f'Não foi possivel transformar a imagem {e}')
