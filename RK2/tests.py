import unittest
from RK2 import Driver, CarPark, DriverAndCarPark, query_1, query_2, query_3

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
carparks_data = [
            CarPark(1, "ЭкоМобиль"),
            CarPark(2, "АвтоОазис"),
            CarPark(3, "Городской Флот"),
            CarPark(4, "Звездный"),
            CarPark(5, "АвтоСпектр")
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

class TestCarParkQueries(unittest.TestCase):
    def test_query_1(self):    
        result = query_1(drivers_data, carparks_data, driver_and_carpark_data)
        expected = [
            "Водитель: Абрамов, Автопарк: Городской Флот",
            "Водитель: Иванов, Автопарк: Звездный",
            "Водитель: Михалёв, Автопарк: ЭкоМобиль",
            "Водитель: Петров, Автопарк: Городской Флот",
            "Водитель: Радченко, Автопарк: АвтоОазис",
            "Водитель: Сидоренко, Автопарк: Городской Флот",
            "Водитель: Сидоров, Автопарк: АвтоСпектр",
            "Водитель: Тюльпанов, Автопарк: АвтоСпектр"
        ]
        self.assertEqual(result, expected)

    def test_query_2(self):
        result = query_2(drivers_data, carparks_data)
        expected = [
            "Автопарк: Городской Флот, Количество водителей: 3",
            "Автопарк: АвтоСпектр, Количество водителей: 2",
            "Автопарк: АвтоОазис, Количество водителей: 1",
            "Автопарк: Звездный, Количество водителей: 1",
            "Автопарк: ЭкоМобиль, Количество водителей: 1"
        ]
        self.assertEqual(result, expected)

    def test_query_3(self):
        result = query_3(drivers_data, carparks_data, driver_and_carpark_data)
        expected = [
            "Водитель: Иванов, Автопарк(и): ЭкоМобиль, Городской Флот, АвтоСпектр",
            "Водитель: Петров, Автопарк(и): АвтоОазис",
            "Водитель: Сидоров, Автопарк(и): ЭкоМобиль, Звездный",
            "Водитель: Абрамов, Автопарк(и): Городской Флот, Звездный",
            "Водитель: Тюльпанов, Автопарк(и): АвтоОазис"
        ]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()


