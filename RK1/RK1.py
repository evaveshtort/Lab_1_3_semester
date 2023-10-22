from collections import Counter
from collections import defaultdict

class Driver:
    def __init__(self, driver_id, surname, salary, carpark_id):
        self.driver_id = driver_id
        self.surname = surname
        self.salary = salary
        self.carpark_id = carpark_id
        
class CarPark:
    def __init__(self, carpark_id, name):
        self.carpark_id = carpark_id
        self.name = name
        
class DriverAndCarPark:
    def __init__(self, driver_id, carpark_id):
        self.driver_id = driver_id
        self.carpark_id = carpark_id
        
carparks_data = [
    CarPark(1, "ЭкоМобиль"),
    CarPark(2, "АвтоОазис"),
    CarPark(3, "Городской Флот"),
    CarPark(4, "Звездный"),
    CarPark(5, "АвтоСпектр")
]

drivers_data = [
    Driver(1, "Иванов", 20000, 4),
    Driver(2, "Петров", 15000, 3),
    Driver(3, "Сидоров", 17000, 5),
    Driver(4, "Михалёв", 21000, 1),
    Driver(5, "Радченко", 23000, 2),
    Driver(6, "Сидоренко", 16000, 3),
    Driver(7, "Абрамов", 20000, 3),
    Driver(8, "Тюльпанов", 18000, 5)
]

driver_and_carpark_data = [
    DriverAndCarPark(1, 1),
    DriverAndCarPark(1, 3),
    DriverAndCarPark(1, 5),
    DriverAndCarPark(2, 2),
    DriverAndCarPark(3, 1),
    DriverAndCarPark(3, 4),
    DriverAndCarPark(4, 2),
    DriverAndCarPark(4, 5),
    DriverAndCarPark(5, 1),
    DriverAndCarPark(5, 2),
    DriverAndCarPark(5, 4),
    DriverAndCarPark(6, 1),
    DriverAndCarPark(7, 3),
    DriverAndCarPark(7, 4),
    DriverAndCarPark(8, 2),
]

#Запрос 1: список всех водителей и их автопарков, отсортированный по имени водителя

print('Запрос 1:')

sorted_drivers = sorted(drivers_data, key=lambda x: x.surname)
carpark_dict = {carpark.carpark_id: carpark.name for carpark in carparks_data}

[print(f"Водитель: {driver.surname}, Автопарк: {carpark_dict.get(driver.carpark_id, 'Неизвестный автопарк')}") for driver in sorted_drivers]

#Запрос 2: список автопарков и количесвта водитеелй в них, отсортированный по количеству водителей

print('\nЗапрос 2:')

num_drivers = Counter(d.carpark_id for d in drivers_data)
sorted_carparks = sorted(carparks_data, key=lambda x: num_drivers[x.carpark_id], reverse=True)

[print(f"Автопарк: {carpark.name}, Количество водителей: {num_drivers[carpark.carpark_id]}") for carpark in sorted_carparks]

#Запрос 3: список водителей, фамилия которых заканчивается на "ов" и их автопарков

print('\nЗапрос 3:')

driver_carpark_dict = defaultdict(list)

for cd in driver_and_carpark_data:
    driver_carpark_dict[cd.driver_id].append(cd.carpark_id)

filtered_drivers = [driver for driver in drivers_data if driver.surname.endswith("ов")]

[print(f"Водитель: {driver.surname}, Автопарк(и): {', '.join(carpark_dict[carpark_id] for carpark_id in driver_carpark_dict.get(driver.driver_id, []))}") for driver in filtered_drivers]
