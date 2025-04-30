from field import Field
from random import randint


def _check_win_status(game_field, time, field):
    if game_field.prince == game_field.princess:
        return True

def add(field, curr_block, prev_blocks):
    if len(prev_blocks) == 0:
        prev_blocks.append(curr_block)
        return
    if curr_block in prev_blocks:
        prev_blocks.pop(-1)
        return

    last_block = prev_blocks[-1]
    game_field = field.game_field
    if game_field[curr_block[0]][curr_block[1]] == game_field[prev_blocks[-1][0]][prev_blocks[-1][1]]\
            and ((abs(last_block[0] - curr_block[0]) == 1 and last_block[1] == curr_block[1]) or (abs(last_block[1] - curr_block[1]) == 1 and last_block[0] == curr_block[0])):
        prev_blocks.append(curr_block)
def delete_blocks(field, blocks_for_delete):
    if len(blocks_for_delete) < 3:
        return
    colors = "pink", "yellow", "purple"
    for row, col in blocks_for_delete:
        x = randint(0, 2)
        field.game_field[row][col] = colors[x]


def _add_block(game_field, curr_block, picked_blocks):
    ...
