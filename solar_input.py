# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet
from solar_vis import DrawableObject

def from_notation(char):
    if len(char.split('e')) == 2:
        return int(char.split('e')[0]) * 10**int(char.split('e')[1])
    else:
        return int(char)

def to_notation(char):
    if char == 0:
        return char
    else:
        return str(char/(10**(len(str(char))-1))) + 'E' + str(len(str(char))-1)

def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename, 'r') as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем

            object_type = line.split()[0].lower()
            if object_type == "star":
                star = Star()
                parse_object_parameters(line, star)
                objects.append(star)
            elif object_type == "planet":
                planet = Planet()
                parse_object_parameters(line, planet)
                objects.append(planet)
            else:
                print("Unknown space object in line\n" + line)

    return [DrawableObject(obj) for obj in objects]


def parse_object_parameters(line, obj):
    """Считывает данные о звезде из строки.

    Входная строка должна иметь слеюущий формат:

    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.

    Пример строки:

    Star 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание звезды.

    **star** — объект звезды.
    """
    line = line.lower().split()
    obj.R = int(line[1])
    obj.color = line[2]
    obj.m = from_notation(line[3])
    obj.x = from_notation(line[4])
    obj.y = from_notation(line[5])
    obj.Vx = from_notation(line[6])
    obj.Vy = from_notation(line[7])
    return obj


def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.

    Строки должны иметь следующий формат:

    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    **output_filename** — имя входного файла

    **space_objects** — список объектов планет и звёзд
    """
    with open(output_filename, 'w') as out_file:
        for obj in space_objects:
            print("%s %d %s %s %s %s %s %s" % (
                obj.type, obj.R, obj.color,
                to_notation(obj.m), to_notation(obj.x), to_notation(obj.y),
                to_notation(obj.Vx), to_notation(obj.Vy)), file = out_file)


if __name__ == "__main__":
    objects = read_space_objects_data_from_file('double_star.txt')
    write_space_objects_data_to_file('test.txt', [A.obj for A in objects])
