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

    def print_info(self):
        print("-" * 30)
        print(f"Имя: {self.__name}")
        print(f"Голод: {self.__hunger}/100")
        print(f"Энергия: {self.__energy}/100")
        print(f"Счастье: {self.__happiness}/100")
        print("-" * 30)

    def feed(self):
        self.__hunger -= 20

        if self.__hunger < 0:
            self.__hunger = 0

        print(f"{self.__name} покушал!")

    def play(self):
        if self.__energy < 15:
            print("Недостаточно энергии!")
            return

        self.__happiness += 20
        self.__energy -= 15
        self.__hunger += 10

        if self.__happiness > 100:
            self.__happiness = 100

        if self.__hunger > 100:
            self.__hunger = 100

        print(f"{self.__name} поиграл!")

    def sleep(self):
        self.__energy += 30
        self.__hunger += 10

        if self.__energy > 100:
            self.__energy = 100

        if self.__hunger > 100:
            self.__hunger = 100

        print(f"{self.__name} поспал!")

    def is_dead(self):
        return self.__energy == 0 and self.__happiness == 0 and self.__hunger == 100
