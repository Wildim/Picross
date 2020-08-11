import pygame
cell_size = 20


def make_matrix(grid_left, grid_top, width, height):
    cells = []
    left = grid_left
    top = grid_top
    cell_width = cell_height = cell_size
    for i in range(0, height):
        for j in range(0, width):
            rect_fit = pygame.Rect(left, top, cell_width, cell_height)
            rect_fill = 1
            cells.append({'rect': rect_fit, 'fill': rect_fill})
            left += cell_size
        left = grid_left
        top += cell_size

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
    if mouse_code == 4:
        cell_size -= 1