class Tamagochi:
    __name: str
    __hunger: int
    __energy: int
    __happiness: int

    def __init__(self, name: str):
        self.__name = name

        self.__hunger = 50
        self.__energy = 100
        self.__happiness = 50

    def set_name(self, name: str):
        if len(name) < 2 or len(name) > 30:
            print("Ошибка. Имя должно быть длинной от 2 до 30 сиволов")
            return

        self.__name = name

    def get_name(self) -> str:
        return self.__name
