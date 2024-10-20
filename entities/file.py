class File:
    def __init__(self, name : str, type : str):
        self._name = name
        self._type = type

    @property
    def name(self) -> str:
        return self._name
    @property
    def type(self) -> str:
        return self._type
    
    @property
    def name_and_type(self) -> str:
        return f'{self.name}.{self.type}'