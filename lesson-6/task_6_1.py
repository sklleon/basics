# 1. Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.

from time import sleep

<< << << < HEAD
# вариант 1
== == == =
>> >> >> > a62a74a9af9301630cc59902d79325a50a4d94ec


class TrafficLight:
    tl_color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        i = 0
        while i != 3:
            print(TrafficLight.tl_color[i])
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(5)
            i += 1


obj = TrafficLight()
obj.running()
<< << << < HEAD


# вариант 2
class Trafficlight:
    __color = {'Крассный': 7, 'Желтый': 2, 'Зеленый': 5}

    @staticmethod
    def running():
        for key, value in Trafficlight.__color.items():
            print(f'Светофор переключается в режиме {key}')
            sleep(value)


TL = Trafficlight()
TL.running()
== == == =
>> >> >> > a62a74a9af9301630cc59902d79325a50a4d94ec
