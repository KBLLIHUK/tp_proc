from Figure_Class import *
from Rectangle import *
from Circle import *
from Color import *

def figure_get_from_file(type, file):
    figure = Figure(type)
    if type == 1:
        figure.void = Circle()
        figure.coord1 = file.readline().strip()
        figure.coord2 = file.readline().strip()
        figure.WhatColor = WhatColor(int(file.readline()))
    if type == 2:
        figure.void = Rectangle()
        figure.coord1 = file.readline().strip()
        figure.coord11 = figure.coord1.split()[0]
        figure.coord1 = figure.coord1.split()[1]
        figure.coord2 = file.readline().strip()
        figure.coord21 = figure.coord2.split()[0]
        figure.coord2 = figure.coord2.split()[1]
        figure.WhatColor = WhatColor(int(file.readline()))
    return figure
