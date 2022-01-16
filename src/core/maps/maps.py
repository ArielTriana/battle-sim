from abc import ABC, abstractclassmethod


class Cell:

    def __init__(self, passable, type, row, column, heigth):
        self.passable = passable
        self.type = type
        self.row = row
        self.col = column
        self.heigth = heigth
        self.bs_object = None


class Map(ABC):

    @abstractclassmethod
    def __init__(self, no_rows, no_columns, sides):
        self.no_rows = no_rows
        self.no_columns = no_columns
        self.sides = sides
        self.matrix = None

    def __getitem__(self, i):
        return self.matrix[i]


class LandMap(Map):

    def __init__(self, no_rows, no_columns, heigth_map, sea_heigth, sides):
        Map.__init__(no_rows, no_columns, sides)
        self.matrix = [[Cell(5, "earth" if heigth_map[i][j] > sea_heigth else "water",
                             i, j, heigth_map[i][j]) for j in range(no_columns)] for i in range(no_rows)]


class AirMap(Map):

    def __init__(self, no_rows, no_columns, sides):
        Map.__init__(no_rows, no_columns, sides)
        self.matrix = [[Cell(5, "air", i, j, None)
                        for j in range(no_columns)] for i in range(no_rows)]