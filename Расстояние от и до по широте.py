
from math import radians, sin, cos, acos


class Point:
    def __init__(self, latitude, longitude):
        self.latitude = radians(latitude)
        self.longitude = radians(longitude)

    # считаем расстояние между двумя точками в км
    def distance(self, other):
        cos_d = sin(self.latitude) * sin(other.latitude) + cos(self.latitude) * cos(other.latitude) * cos(
            self.longitude - other.longitude)
        return f'Расстояние от москвы до эвереста: {6371 * acos(cos_d)} км'


class City(Point):
    def __init__(self, latitude, longitude, name, population):
        super().__init__(latitude, longitude)
        # допишите код: сохраните свойства родителя
        self.name = name
        self.population = population
        # и добавьте свойства name и population

    def show(self):
        print(f"Город {self.name}, население {self.population} чел.")


class Mountain(Point):
    def __init__(self, latitude, longitude, name, height):
        # допишите код: напишите конструктор, в нём сохраните свойства родителя
        super().__init__(latitude, longitude,)
        # и добавьте свойства name и height
        self.name = name
        self.height = height

    # Переопределите метод show(self):
    # информацию о горе нужно вывести в формате:
    # "Высота горы <название> - <высота> м."
    def show(self):
        print(f"Высота горы {self.name} - {self.height} м.")


moscow = City(56, 38, 'Москва', '11,92 милионов')
everest = Mountain(27.988056, 86.925278, 'Эверест', '8 849', )


moscow.show()
everest.show()

print(moscow.distance(everest))
