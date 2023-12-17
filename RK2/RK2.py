from collections import Counter, defaultdict

class CarPark:
    def __init__(self, carpark_id, name):
        self.carpark_id = carpark_id
        self.name = name

class Driver:
    def __init__(self, driver_id, surname, salary, carpark_id):
        self.driver_id = driver_id
        self.surname = surname
        self.salary = salary
        self.carpark_id = carpark_id

class DriverAndCarPark:
    def __init__(self, driver_id, carpark_id):
        self.driver_id = driver_id
        self.carpark_id = carpark_id

def get_sorted_drivers(drivers_data):
    return sorted(drivers_data, key=lambda x: x.surname)

def get_carpark_dict(carparks_data):
    return {carpark.carpark_id: carpark.name for carpark in carparks_data}

def query_1(drivers_data, carparks_data, driver_and_carpark_data):
    sorted_drivers = get_sorted_drivers(drivers_data)
    carpark_dict = get_carpark_dict(carparks_data)
    result = []
    for driver in sorted_drivers:
        carpark_name = carpark_dict.get(driver.carpark_id, 'Неизвестный автопарк')
        result.append(f"Водитель: {driver.surname}, Автопарк: {carpark_name}")
    return result

def query_2(drivers_data, carparks_data):
    num_drivers = Counter(d.carpark_id for d in drivers_data)
    sorted_carparks = sorted(carparks_data, key=lambda x: x.name)
    sorted_carparks = sorted(sorted_carparks, key=lambda x: num_drivers[x.carpark_id], reverse=True)
    result = []
    for carpark in sorted_carparks:
        result.append(f"Автопарк: {carpark.name}, Количество водителей: {num_drivers[carpark.carpark_id]}")
    return result

def query_3(drivers_data, carparks_data, driver_and_carpark_data):
    driver_carpark_dict = defaultdict(list)
    carpark_dict = get_carpark_dict(carparks_data)
    for cd in driver_and_carpark_data:
        driver_carpark_dict[cd.driver_id].append(cd.carpark_id)
    filtered_drivers = [driver for driver in drivers_data if driver.surname.endswith("ов")]
    result = []
    for driver in filtered_drivers:
        carparks = [carpark_dict[carpark_id] for carpark_id in driver_carpark_dict.get(driver.driver_id, [])]
        result.append(f"Водитель: {driver.surname}, Автопарк(и): {', '.join(carparks)}")
    return result

