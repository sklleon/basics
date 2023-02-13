# 2. Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.

class Road:

    << << << < HEAD
self.weight = 25
self.height = 5
== == == =
>> >> >> > a62a74a9af9301630cc59902d79325a50a4d94ec


def __init__(self, length, width):
    self._length = length
    self._width = width

<< << << < HEAD


def asphalt_mass(self):
    asphalt_mass = self._length * self._width * self.weight * self.height / 1000
    print(f'Для покрытия всего дорожного полотна потребуются {round(asphalt_mass)} тонн асфальта')

== == == =
self.weight = 25
self.height = 5


def asphalt_mass(self):
    asphalt_mass = self._length * self._width * self.weight * self.height / 1000
    print(f'Для покрытия всего дорожного полотна неободимо {round(asphalt_mass)} массы асфальта')

>> >> >> > a62a74a9af9301630cc59902d79325a50a4d94ec

obj = Road(5000, 20)
obj.asphalt_mass()
