from car import Car

global_car_id = 0


def get_next_car_id():
    global global_car_id

    global_car_id += 1

    return global_car_id


def input_car_data() -> Car:
    brand = input("введите марку автомобиля: ")
    model = input("введите модель автомобиля: ")
    price = int(input("введите цену автомобиля: "))
    photo_url = input("введите url фото автомобиля: ")

    return Car(brand=brand, model=model, price=price, photo_url=photo_url)


def add_new_car(cars: list[Car], new_car: Car):
    cars.append(new_car)


def get_car_by_id(cars: list[Car], id: int) -> Car | None:
    for car in cars:
        if car.id == id:
            return car

    return None


def update_car_by_id(cars: list[Car], car: Car) -> bool:
    found_car = get_car_by_id(cars, car.id)

    if found_car == None:
        return False

    found_car.brand = car.brand
    found_car.model = car.model
    found_car.price = car.price
    found_car.photo_url = car.photo_url

    return True


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


def fill_cars_mock_data(cars: list[Car]):
    car1 = Car(
        brand="Tesla",
        model="Model 3",
        price=5400000,
        photo_url="https://example.com",
        id=get_next_car_id(),
    )

    car2 = Car(
        brand="BMW",
        model="M5",
        price=14500000,
        photo_url="https://example.com",
        id=get_next_car_id(),
    )

    car3 = Car(
        brand="Toyota",
        model="RAV4",
        price=4200000,
        photo_url="https://example.com",
        id=get_next_car_id(),
    )

    car4 = Car(
        brand="Porsche",
        model="911 Carrera",
        price=18500000,
        photo_url="https://example.com",
        id=get_next_car_id(),
    )

    car5 = Car(
        brand="Hyundai",
        model="Ioniq 5",
        price=5900000,
        photo_url="https://example.com",
        id=get_next_car_id(),
    )

    add_new_car(cars, car1)
    add_new_car(cars, car2)
    add_new_car(cars, car3)
    add_new_car(cars, car4)
    add_new_car(cars, car5)
