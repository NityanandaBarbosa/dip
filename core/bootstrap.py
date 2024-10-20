import os
import platform
import importlib
import inspect
from . import ImageTransformer, Paths

class Bootstrap:
    def _get_usecases(self) -> list[ImageTransformer]:
        transformers : list[ImageTransformer] = []
        for arquivo in os.listdir(Paths.USECASES):
            if arquivo.endswith('.py') and arquivo != '__init__.py':
                caminho_arquivo = os.path.join(Paths.USECASES, arquivo)
                spec = importlib.util.spec_from_file_location(arquivo[:-3], caminho_arquivo)
                modulo = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(modulo)

                for nome, obj in inspect.getmembers(modulo):
                    if inspect.isclass(obj) and issubclass(obj, ImageTransformer) and obj != ImageTransformer:
                        instancia = obj()
                        transformers.append(instancia)

        return transformers
    
    def _choose_usecase(self, usecases : list[ImageTransformer]) -> ImageTransformer:
        print("Escolha um nome da lista:")
        for index, usecase in enumerate(usecases):
            print(f"{index}: {usecase.algorithm_name}")
        while True:
            try:
                choice = int(input("Digite o índice do nome que deseja escolher: "))
                if 0 <= choice < len(usecases):
                    print(f"Você escolheu: {usecases[choice].algorithm_name}")
                    return usecases[choice]
                else:
                    self._clear_terminal()
                    print("Índice inválido. Tente novamente.")
                    return self._choose_usecase(usecases= usecases)
            except ValueError:
                self._clear_terminal()
                print("Por favor, digite um número válido.")
                return self._choose_usecase(usecases= usecases)
    
    def _clear_terminal(self):
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")
    
    def execute(self):
        usecases = self._get_usecases()
        usecase = self._choose_usecase(usecases=usecases)
        usecase.execute(image_path=f'{Paths.INPUT}building.jpg')
