# Экземпляр класса хранит имя и текущие показатели одного питомца.
class Tamagochi:
    # Аннотации указывают типы атрибутов. Двойное подчёркивание в начале
    # имени защищает внутренние атрибуты от случайных совпадений имён.
    __name: str
    __hunger: int
    __energy: int
    __happiness: int

    def __init__(self, name: str):
        # При создании питомца сохраняем переданное имя и задаём
        # начальные показатели. Энергия начинает со 100 из 100.
        self.__name = name

        self.__hunger = 50
        self.__energy = 100
        self.__happiness = 50

    def set_name(self, name: str):
        # Разрешаем имена длиной от 2 до 30 символов включительно.
        # При ошибке return завершает метод до присваивания, сохраняя старое имя.
        if len(name) < 2 or len(name) > 30:
            print("Ошибка. Имя должно быть длинной от 2 до 30 сиволов")
            return

        self.__name = name

    def get_name(self) -> str:
        # Возвращаем имя, чтобы его можно было использовать в другом коде.
        return self.__name

    def print_info(self):
        # Выводим имя и показатели по шкале от 0 до 100.
        # Умножение строки на 30 создаёт строку-разделитель из дефисов.
        print("-" * 30)
        print(f"Имя: {self.__name}")
        print(f"Голод: {self.__hunger}/100")
        print(f"Энергия: {self.__energy}/100")
        print(f"Счастье: {self.__happiness}/100")
        print("-" * 30)

    def feed(self):
        # Чем меньше значение голода, тем сытнее питомец.
        # Кормление убирает до 20 единиц голода, но ниже нуля он не опускается.
        self.__hunger -= 20

        if self.__hunger < 0:
            self.__hunger = 0

        print(f"{self.__name} покушал!")

    def play(self):
        # Игра требует как минимум 15 единиц энергии. Если энергии
        # не хватает, выходим из метода до изменения показателей.
        if self.__energy < 15:
            print("Недостаточно энергии!")
            return

        # Игра приносит 20 единиц счастья, расходует 15 единиц энергии
        # и повышает голод на 10 единиц.
        self.__happiness += 20
        self.__energy -= 15
        self.__hunger += 10

        # Ограничиваем выросшие показатели верхней границей шкалы.
        if self.__happiness > 100:
            self.__happiness = 100

        if self.__hunger > 100:
            self.__hunger = 100

        print(f"{self.__name} поиграл!")

    def sleep(self):
        # Сон восстанавливает 30 единиц энергии и повышает голод на 10.
        # Каждый из этих показателей ограничен максимумом 100.
        self.__energy += 30
        self.__hunger += 10

        if self.__energy > 100:
            self.__energy = 100

        if self.__hunger > 100:
            self.__hunger = 100

        print(f"{self.__name} поспал!")

    def is_dead(self):
        # and возвращает True, только когда все три условия выполнены одновременно:
        # энергия и счастье равны нулю, а голод достиг 100.
        return self.__energy == 0 and self.__happiness == 0 and self.__hunger == 100
