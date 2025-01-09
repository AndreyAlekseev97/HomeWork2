class Vehicle:
    __COLOR_VARIANTS = ['yellow', 'grey', 'black', 'red', 'white']
    def __init__(self, owner: str, __model: str, __engine_power: int, __color: str):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    def get_model (self):
        return f'Модель: {self.__model}'

    def get_horspower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет транспорта: {self.__color}'

    def print_info(self):
        print(self.get_model())
        print(self.get_horspower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color: str):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')

class Sedan(Vehicle):
    __PASSENGER_LIMIT = 5

vehicle1 = Vehicle('Andrey', 'Subaru Forester', 280, 'grey' )
vehicle1.print_info()

vehicle1.set_color('Blue')
vehicle1.set_color('BLACK')

vehicle1.print_info()