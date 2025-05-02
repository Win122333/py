from random import randint


def check_win_status(field, time=0):
    if time > field.time: return False
    if field.prince == field.princess - 1:
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
    if game_field[curr_block[0]][curr_block[1]] == game_field[prev_blocks[-1][0]][prev_blocks[-1][1]] \
            and ((abs(last_block[0] - curr_block[0]) == 1 and last_block[1] == curr_block[1]) or (
            abs(last_block[1] - curr_block[1]) == 1 and last_block[0] == curr_block[0])):
        prev_blocks.append(curr_block)


def delete_blocks(field, blocks_for_delete):
    def get_cost():
        color = field.game_field[blocks_for_delete[0][0]][blocks_for_delete[0][1]]
        if color == "yellow":
            cost = 100
        elif color == "pink":
            cost = 200
        elif color == "purple":
            cost = 500
        return cost
    def shift_down(times=1):
        for i in range(times):
            for row in range(len(field.game_field) - 1, 0, -1):
                for col in range(len(field.game_field[0])):
                    if field.game_field[row][col] is None:
                        field.game_field[row][col] = field.game_field[row - 1][col]
                        field.game_field[row - 1][col] = None

    def fill():
        colors = ["pink", "yellow", "purple"]
        for row in range(len(field.game_field)):
            for col in range(len(field.game_field[row])):
                if field.game_field[row][col] is None:
                    field.game_field[row][col] = colors[randint(0, 2)]

    if len(blocks_for_delete) < 3:
        return
    for row, col in blocks_for_delete:
        field.game_field[row][col] = None
    shift_down(len(blocks_for_delete))
    fill()
    return get_cost() * len(blocks_for_delete)
