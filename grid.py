import pygame
from consts import DISPLAY_WIDTH, DISPLAY_HEIGHT
cell_size = 20
grid_size = grid_width, grid_height = 5, 5


def get_grid_start_pos():
    grid_start_pos = [DISPLAY_WIDTH / 2 - (grid_width / 2) * cell_size,
                      DISPLAY_HEIGHT / 2 - (grid_height / 2) * cell_size]

    return grid_start_pos


def make_matrix(cells=None):
    if not cells:
        cells = []
        left, top = get_grid_start_pos()
        start_left = left
        cell_width = cell_height = cell_size
        for i in range(0, grid_height):
            for j in range(0, grid_width):
                rect_fit = pygame.Rect(left, top, cell_width, cell_height)
                rect_fill = 1
                row = i
                col = j
                cells.append({'row': row, 'col': col, 'rect': rect_fit, 'fill': rect_fill})
                left += cell_size
            left = start_left
            top += cell_size
    else:
        left, top = get_grid_start_pos()
        start_left = left
        for rect in cells:
            cell_width = cell_height = cell_size
            rect['rect'].left = left
            rect['rect'].top = top
            rect['rect'].width = cell_width
            rect['rect'].height = cell_height
            left += cell_size
            if rect['col'] == grid_width - 1:
                left = start_left
                top += cell_size
    for rect in cells:
        print(rect)
    return cells


def fill_cell(grid, mouse_coord):
    for rect in grid:
        if rect['rect'].collidepoint(mouse_coord):
            if rect['fill'] == 1:
                rect['fill'] = 0
            else:
                rect['fill'] = 1
            break

    return grid


def grid_resize(grid, mouse_code):
    global cell_size
    if mouse_code == 4:
        cell_size += 1
    elif mouse_code == 5:
        cell_size -= 1

    grid = make_matrix(grid)
    return grid
