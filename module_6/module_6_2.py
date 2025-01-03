# Задача "Изменять нельзя получать"

class Vehicle:
    __COLOR_VARIANTS = ['Red', 'Green', 'Blue', 'White', 'Black', 'Yellow', 'Gray']   # Допустимые цвета для окрашивания
    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = str(owner)         # Владелец транспорта. (владелец может меняться)
        self.__model = str(__model)    # Модель (марка) транспорта. (мы не можем менять название модели)
        self.__engine_power = int(__engine_power)   # Мощность двигателя. (мы не можем менять самостоятельно)
        self.__color = str(__color)     # Название цвета. (мы не можем менять цвет автомобиля своими руками)

# Каждый объект Vehicle должен содержать следующий методы:
    def get_model(self):
        print(f'Модель: {self.__model}')

    def get_horsepower(self):
        print(f'Мощность двигателя: {self.__engine_power} лошадиных сил ')

    def get_color(self):
        print(f'Цвет: {self.__color.upper()}')

    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print(f'Владелец: {self.owner}\n')

    def set_color(self, new_color):
        # new_color = input('Новый цвет: ')
        reg_colours = [colour.lower() for colour in self.__COLOR_VARIANTS] # для проверки без учета регистра
        if new_color.lower() in reg_colours:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}\n')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 4      # (в седан может поместиться только 4 пассажира и 1 водитель)


vehicle1 = Sedan('Fedos', 'Toyota Mark II',  500, 'blue')
# Изначальные свойства
vehicle1.print_info()
# Меняем свойства (в т.ч. Вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
# Проверяем что поменялось

vehicle1.print_info()

