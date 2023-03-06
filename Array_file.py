from Figure_to import *


def Array_record_to_file(array, file):
    file.write(f"Записано {array.size} фигры\n\n")
    for i in range(array.size):
        figure_record_to_file(array.content[i], file)
