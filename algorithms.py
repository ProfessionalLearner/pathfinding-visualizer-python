from typing import List
from node import GridNode
from a_star import a_star_find_path
from dijkstra import dijkstra_find_path
from breadth_first_search import breadth_first_search_find_path
from depth_first_search import depth_first_search_find_path
from best_first_search import best_first_search_find_path
from tkinter import messagebox
from text_for_application import PATH_NOT_FOUND, TITLE
import pygame


def make_path(draw, start, end):
    node = end.get_parent()
    clock = pygame.time.Clock()
    while node != start:
        clock.tick(50)
        node.mark_path()
        node = node.get_parent()
        draw()


def path_finding_algorithm(draw, grid: List[List[GridNode]], start: GridNode, end: GridNode, speed: int,
                           algo_type: str):
    found_path = ALGORITHMS[algo_type](draw, grid, start, end, speed)
    if found_path:
        make_path(draw, start, end)
    else:
        messagebox.showinfo(TITLE, PATH_NOT_FOUND)


ALGORITHMS = {"A*": a_star_find_path,
              "Best First Search": best_first_search_find_path,
              "Breadth First Search": breadth_first_search_find_path,
              "Depth First Search": depth_first_search_find_path,
              "Dijkstra": dijkstra_find_path}

ALGORITHMS_LIST = ALGORITHMS.keys()
