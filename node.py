import pygame
import math
from typing import List
from colors import ColorRGB


class GridNode:
    def __init__(self, row: int, col: int, width: int,
                 height: int, total_rows: int, total_cols: int):
        self.row = row
        self.col = col
        self.x = col * width
        self.y = row * height
        self.color = ColorRGB.WHITE
        self.neighbours = []
        self.width = width
        self.height = height
        self.total_rows = total_rows
        self.total_cols = total_cols
        self.parent = None

    def set_parent(self, other):
        self.parent = other

    def get_parent(self):
        return self.parent

    def get_position(self):
        return self.row, self.col

    def is_finished(self):
        return self.color == ColorRGB.RED

    def is_visited(self):
        return self.color == ColorRGB.LIME

    def is_barrier(self):
        return self.color == ColorRGB.BLACK

    def is_start(self):
        return self.color == ColorRGB.ORANGE

    def is_end(self):
        return self.color == ColorRGB.BLUE

    def reset_node(self):
        self.parent = None
        self.color = ColorRGB.WHITE

    def mark_as_finished(self):
        self.color = ColorRGB.RED

    def mark_as_visited(self):
        self.color = ColorRGB.LIME

    def mark_as_end(self):
        self.color = ColorRGB.BLUE

    def mark_as_start(self):
        self.color = ColorRGB.ORANGE

    def mark_as_barrier(self):
        self.color = ColorRGB.BLACK

    def mark_path(self):
        self.color = ColorRGB.PURPLE

    def draw(self, win):
        pygame.draw.rect(win, self.color.value, (self.x, self.y, self.width, self.height))

    def update_neighbours(self, grid, allow_diagonals: int):
        self.parent = None
        self.neighbours = []

        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier():  # lower neighbour
            dist_from_parent = self.height
            self.neighbours.append([grid[self.row + 1][self.col], dist_from_parent])

        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():  # upper neighbour
            dist_from_parent = self.height
            self.neighbours.append([grid[self.row - 1][self.col], dist_from_parent])

        if self.col < self.total_cols - 1 and not grid[self.row][self.col + 1].is_barrier():  # right neighbour
            dist_from_parent = self.width
            self.neighbours.append([grid[self.row][self.col + 1], dist_from_parent])

        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():  # left neighbour
            dist_from_parent = self.width
            self.neighbours.append([grid[self.row][self.col - 1], dist_from_parent])

        if allow_diagonals:
            self.add_diagonal_neighbours(grid)

    def add_diagonal_neighbours(self, grid):
        dist_from_parent = int(math.sqrt(self.height ** 2 + self.width ** 2))

        if self.row > 0 and self.col > 0 \
                and not grid[self.row - 1][self.col - 1].is_barrier():  # upper left neighbour
            self.neighbours.append([grid[self.row - 1][self.col - 1], dist_from_parent])

        if self.row > 0 and self.col < self.total_cols - 1 \
                and not grid[self.row - 1][self.col + 1].is_barrier():  # upper right neighbour
            self.neighbours.append([grid[self.row - 1][self.col + 1], dist_from_parent])

        if self.row < self.total_rows - 1 and self.col < self.total_cols - 1 \
                and not grid[self.row + 1][self.col + 1].is_barrier():  # lower right neighbour
            self.neighbours.append([grid[self.row + 1][self.col + 1], dist_from_parent])

        if self.row < self.total_rows - 1 and self.col > 0 \
                and not grid[self.row + 1][self.col - 1].is_barrier():  # lower left neighbour
            self.neighbours.append([grid[self.row + 1][self.col - 1], dist_from_parent])

    def get_neighbours(self):
        return self.neighbours

    def __lt__(self, other):
        return False
