from enum import Enum


class Block(Enum):
    PRINCESS = 'princess'
    PRINCE = 'prince'
    YELLOW_BLOCK = 'yellow'
    PINK_BLOCK = 'pink'
    PURPLE_BLOCK = 'purple'


    def __call__(self):
        return self.value