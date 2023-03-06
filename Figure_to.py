from Color import *


def figure_record_to_file(figure, file):
    if figure.type == 1:
        file.write(f"Круг центр {figure.coord1}, радиус {figure.coord2}\n")
        if figure.WhatColor == WhatColor.red:
            file.write(f"Красный")
        elif figure.WhatColor == WhatColor.orange:
            file.write(f"Оранжевый")
        elif figure.WhatColor == WhatColor.yellow:
            file.write(f"Желтый")
        elif figure.WhatColor == WhatColor.green:
            file.write(f"Зеленый")
        elif figure.WhatColor == WhatColor.cyan:
            file.write(f"Голубой")
        elif figure.WhatColor == WhatColor.blue:
            file.write(f"Синий")
        else:
            file.write("Фиолетовый")
        file.write('\n\n')
    if figure.type == 2:
        file.write(
            f"Прямоугольник [{figure.coord11},{figure.coord1}] [{figure.coord21},{figure.coord2}]\n")
        if figure.WhatColor == WhatColor.red:
            file.write(f"Красный")
        elif figure.WhatColor == WhatColor.orange:
            file.write(f"Оранжевый")
        elif figure.WhatColor == WhatColor.yellow:
            file.write(f"Желтый")
        elif figure.WhatColor == WhatColor.green:
            file.write(f"Зеленый")
        elif figure.WhatColor == WhatColor.cyan:
            file.write(f"Голубой")
        elif figure.WhatColor == WhatColor.blue:
            file.write(f"Синий")
        else:
            file.write("Фиолетовый")
        file.write('\n\n')
