import pygame
import field
from blocks import Block
from copy import deepcopy
from game import delete_blocks, add
from colors import Color


PINK_BLOCK, YELLOW_BLOCK, PURPLE_BLOCK, PRINCE_BLOCK, PRINCESS_BLOCK, BACKGROUND = None, None, None, None, None, None
level_field = field.Field('field_lvl1.txt')
temp_field = deepcopy(level_field)
SIZE_OF_BLOCK = 35
blocks = []
mouse_clicked = False
mouse_dragged = False
curr_block = None




def run_game():
    global mouse_clicked, mouse_dragged, level_field, curr_block, temp_field, blocks
    screen = init()
    game_area = screen.subsurface(pygame.Rect(300, 100, 200, 400))
    pygame.display.set_caption("Кисталлики принцеса драконы весело круто")
    clock = pygame.time.Clock()

    RUN = True
    while RUN:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_clicked = True
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_clicked = False
                mouse_dragged = False
                delete_blocks(temp_field, blocks)
                blocks = []
            elif event.type == pygame.MOUSEMOTION:
                if mouse_clicked:
                    mouse_dragged = True
                    curr_block = take_block(event.pos, SIZE_OF_BLOCK, (8, 5))
                    if curr_block is not None:
                        if len(blocks) == 0:
                            add(temp_field, curr_block, blocks)
                        elif curr_block != blocks[-1]:
                            add(temp_field, curr_block, blocks)

        # Отрисовка
        screen.fill((0, 0, 0))  # Очищаем экран
        draw(temp_field, game_area, blocks)  # Передаем список выделенных блоков
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


def draw(field, screen, selected_blocks):
    highlight_surface = pygame.Surface((SIZE_OF_BLOCK, SIZE_OF_BLOCK), pygame.SRCALPHA)
    highlight_surface.fill(Color.HIGHLIGHT_COLOR.value)

    for row in range(len(field.game_field)):
        for col in range(len(field.game_field[0])):
            x = col * SIZE_OF_BLOCK
            y = row * SIZE_OF_BLOCK
            rect = pygame.Rect(x, y, SIZE_OF_BLOCK, SIZE_OF_BLOCK)

            # Отрисовка самого блока
            if field.game_field[row][col] == Block.PINK_BLOCK():
                screen.blit(PINK_BLOCK, (x, y))
            elif field.game_field[row][col] == Block.YELLOW_BLOCK():
                screen.blit(YELLOW_BLOCK, (x, y))
            elif field.game_field[row][col] == Block.PURPLE_BLOCK():
                screen.blit(PURPLE_BLOCK, (x, y))
            elif field.game_field[row][col] == Block.PRINCE():
                screen.blit(PRINCE_BLOCK, (x, y))
            elif field.game_field[row][col] == Block.PRINCESS():
                screen.blit(PRINCESS_BLOCK, (x, y))

            if (row, col) in selected_blocks:
                screen.blit(highlight_surface, (x, y))
                pygame.draw.rect(screen, Color.BORDER_COLOR.value, rect, 3)


def take_block(mouse_pos, block_size, grid_size):
    x, y = mouse_pos
    x -= 300  # Учитываем смещение игровой области
    y -= 100
    if x < 0 or y < 0:
        return None
    col = x // block_size
    row = y // block_size
    if 0 <= row < grid_size[0] and 0 <= col < grid_size[1]:
        return (row, col)
    return None


def init():
    global PINK_BLOCK, YELLOW_BLOCK, PURPLE_BLOCK, PRINCE_BLOCK, PRINCESS_BLOCK
    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    try:
        # Загрузка и масштабирование изображений
        PINK_BLOCK = pygame.image.load('/Users/win122333/PycharmProjects/pyMain/game/photos/pink.png').convert_alpha()
        PINK_BLOCK = pygame.transform.scale(PINK_BLOCK, (SIZE_OF_BLOCK, SIZE_OF_BLOCK))
        YELLOW_BLOCK = pygame.image.load(
            '/Users/win122333/PycharmProjects/pyMain/game/photos/yellow.png').convert_alpha()
        YELLOW_BLOCK = pygame.transform.scale(YELLOW_BLOCK, (SIZE_OF_BLOCK, SIZE_OF_BLOCK))
        PURPLE_BLOCK = pygame.image.load(
            '/Users/win122333/PycharmProjects/pyMain/game/photos/purple.png').convert_alpha()
        PURPLE_BLOCK = pygame.transform.scale(PURPLE_BLOCK, (SIZE_OF_BLOCK, SIZE_OF_BLOCK))
        PRINCE_BLOCK = pygame.image.load(
            '/Users/win122333/PycharmProjects/pyMain/game/photos/prince.png').convert_alpha()
        PRINCE_BLOCK = pygame.transform.scale(PRINCE_BLOCK, (SIZE_OF_BLOCK, SIZE_OF_BLOCK))
        PRINCESS_BLOCK = pygame.image.load(
            '/Users/win122333/PycharmProjects/pyMain/game/photos/princess.png').convert_alpha()
        PRINCESS_BLOCK = pygame.transform.scale(PRINCESS_BLOCK, (SIZE_OF_BLOCK, SIZE_OF_BLOCK))

    except pygame.error as e:
        print(f"Ошибка загрузки изображения: {e}")
        # Создаем цветные заглушки
        PINK_BLOCK = pygame.Surface((SIZE_OF_BLOCK, SIZE_OF_BLOCK), pygame.SRCALPHA)
        PINK_BLOCK.fill((255, 192, 203, 255))
        YELLOW_BLOCK = pygame.Surface((SIZE_OF_BLOCK, SIZE_OF_BLOCK), pygame.SRCALPHA)
        YELLOW_BLOCK.fill((255, 255, 0, 255))
        PURPLE_BLOCK = pygame.Surface((SIZE_OF_BLOCK, SIZE_OF_BLOCK), pygame.SRCALPHA)
        PURPLE_BLOCK.fill((128, 0, 128, 255))
        PRINCE_BLOCK = pygame.Surface((SIZE_OF_BLOCK, SIZE_OF_BLOCK), pygame.SRCALPHA)
        PRINCE_BLOCK.fill((0, 0, 255, 255))
        PRINCESS_BLOCK = pygame.Surface((SIZE_OF_BLOCK, SIZE_OF_BLOCK), pygame.SRCALPHA)
        PRINCESS_BLOCK.fill((255, 0, 255, 255))

    return screen


if __name__ == '__main__':
    run_game()