from zadanie_5_2 import *

r1 = module1.Room(3, 3.5, 2.7)
print("Размер помещения:", r1.fullSerface()) #общая площадь квартиры
r1.addWD(0.7, 2) #площадь окна
r1.addWD(1.5, 1.6) #площадь окна

print("Площадь оклейки",round(r1.workSurface(),2))

print("Размер рулона:")
d = float(input("Длина - "))
s = float(input("Ширина - "))
print("Количество рулонов:", r1.wallpapers(d, s))
