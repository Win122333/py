from blocks import Block
from copy import deepcopy

def read_field(file_name):
    with open(file_name) as file:
        matr = [i.split() for i in file.readlines()]
        return matr


class Field:
    def __init__(self, file_name):
        try:
            self.game_field = read_field(file_name)
        except FileNotFoundError:
            print("Ошибка: файл уровня не найден!")
            exit()
        self.WIDTH = len(self.game_field)
        self.LENGTH = len(self.game_field[0])

    def __deepcopy__(self, memo):
        # Создаем новый объект без вызова __init__
        new_field = object.__new__(Field)
        # Копируем все атрибуты
        new_field.game_field = deepcopy(self.game_field, memo)
        new_field.WIDTH = self.WIDTH
        new_field.LENGTH = self.LENGTH
        return new_field

    @property
    def princess(self):
        for row in range(len(self.game_field)):
            for col in range(len(self.game_field[0])):
                if self.game_field[row][col] == Block.PRINCESS:
                    return row
        return -1

    @property
    def prince(self):
        for row in range(len(self.game_field)):
            for col in range(len(self.game_field[0])):
                if self.game_field[row][col] == Block.PRINCE:
                    return row
        return -1