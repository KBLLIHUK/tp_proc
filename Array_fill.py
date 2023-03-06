from Figure_from import *
from Array_app import *


def Array_fill(Array, file):
    type = file.readline()
    while type != '' and type != '\n':
        type = int(type)
        figure = figure_get_from_file(type, file)
        Array_append(Array, figure)
        type = file.readline()
