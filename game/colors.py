from enum import Enum


class Color(Enum):
    WHITE = (255, 255, 255)
    PINK = (255, 0, 255)
    PURPLE = (75, 0, 130)
    YELLOW = (255, 255, 0)
    HIGHLIGHT_COLOR = (255, 255, 0, 128)
    BORDER_COLOR = (255, 215, 0)

    def __call__(self):
        return self.value
