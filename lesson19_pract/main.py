from car import Car
from cars_functions import *

global_car_id = 0


def get_next_car_id():
    global global_car_id

    global_car_id += 1

    return global_car_id


cars: list[Car] = []

new_car = input_car_data()
new_car.id = get_next_car_id()

add_new_car(cars, new_car)

new_car = input_car_data()
new_car.id = get_next_car_id()

add_new_car(cars, new_car)


print_all_cars(cars)
