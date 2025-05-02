import math

from blocks import Block
from copy import deepcopy

def read_field(file_name):
    with open(file_name) as file:
        time = int(file.readline())
        matr = [i.split() for i in file.readlines()]
        return matr, time


class Field:
    def __init__(self, file_name):
        try:
            self.game_field, self.time = read_field(file_name)
        except FileNotFoundError:
            print("Ошибка: файл уровня не найден!")
            exit()
        self.HEIGHT = len(self.game_field)
        self.WIDTH = len(self.game_field[0])

    def __deepcopy__(self, memo):
        new_field = object.__new__(Field)
        new_field.game_field = deepcopy(self.game_field, memo)
        new_field.WIDTH = self.WIDTH
        new_field.LENGTH = self.HEIGHT
        return new_field

    @property
    def princess(self):
        for row in range(self.HEIGHT - 1, 0, -1):
            if self.game_field[row][math.floor(self.WIDTH / 2)] == Block.PRINCESS():
                return row
        return -1

    @property
    def prince(self):
        for row in range(self.HEIGHT):
            if self.game_field[row][math.floor(self.WIDTH / 2)] == Block.PRINCE():
                return row
        return -1