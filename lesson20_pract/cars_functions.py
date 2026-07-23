from car import Car


def input_car_data() -> Car:
    brand = input("введите марку автомобиля: ")
    model = input("введите модель автомобиля: ")
    price = int(input("введите цену автомобиля: "))
    photo_url = input("введите url фото автомобиля: ")

    return Car(brand=brand, model=model, price=price, photo_url=photo_url)


def add_new_car(cars: list[Car], new_car: Car):
    cars.append(new_car)


def print_one_car(car: Car):
    print("=" * 20)
    print(f"ИД: {car.id}")
    print(f"Марка: {car.brand}")
    print(f"Модель: {car.model}")
    print(f"Цена (руб.): {car.price}")
    print(f"URL фото: {car.photo_url}")
    print("=" * 20)


def print_all_cars(cars: list[Car]):
    for car in cars:
        print_one_car(car)
