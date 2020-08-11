import sys
import pygame
from grid import make_matrix, fill_cell, grid_resize
from consts import *

pygame.init()

screen = pygame.display.set_mode(DISPLAY_SIZE)
main_grid = make_matrix()


def draw_grid(grid):
    # pygame.draw.line(screen, red, [display_width // 2, 0], [display_width // 2, display_height])
    # pygame.draw.line(screen, red, [0, display_height // 2], [display_width, display_height // 2])

    for rect in grid:
        pygame.draw.rect(screen, WHITE, rect['rect'], rect['fill'])
    # dx = cell_size * width
    # dy = 0
    #
    # for i in range(0, height + 1):
    #     line_start_pos = cell_start_pos[0], cell_start_pos[1] + dy
    #     line_end_pos = cell_start_pos[0] + dx, cell_start_pos[1] + dy
    #     if i == 0 or (i % 5 == 0) or i == height:
    #         line_width = 3
    #     pygame.draw.line(screen, white, line_start_pos, line_end_pos, line_width)
    #     line_width = 1
    #     dy += cell_size
    #
    # dx = 0
    # dy = cell_size * height
    #
    # for i in range(0, width + 1):
    #     line_start_pos = cell_start_pos[0] + dx, cell_start_pos[1]
    #     line_end_pos = cell_start_pos[0] + dx, cell_start_pos[1] + dy
    #     if i == 0 or (i % 5 == 0) or i == width:
    #         line_width = 3
    #     pygame.draw.line(screen, white, line_start_pos, line_end_pos, line_width)
    #     line_width = 1
    #     dx += cell_size


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                main_grid = fill_cell(main_grid, event.pos)
            if event.button == 4 or event.button == 5:
                main_grid = grid_resize(main_grid, event.button)

    # pygame.draw.rect(screen, red, (10, 10, 30, 30)
    screen.fill(BLACK)
    draw_grid(main_grid)
    pygame.display.flip()
