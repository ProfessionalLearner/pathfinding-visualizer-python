from typing import List
from node import GridNode
import pygame


def depth_first_search_find_path(draw, grid: List[List[GridNode]], start: GridNode, end: GridNode, speed: int):
    distances = {node: float("inf") for row in grid for node in row}
    distances[start] = 0

    stack = [start]
    visited = {start}

    clock = pygame.time.Clock()

    while not len(stack) == 0:
        for event in pygame.event.get():
            if event == pygame.QUIT:
                pygame.quit()

        curr_node = stack.pop()

        clock.tick(speed)
        if curr_node == end:
            end.mark_as_end()
            return True

        for neighbour in curr_node.get_neighbours():
            neighbour_node = neighbour[0]
            dist_from_parent = neighbour[1]
            if neighbour_node not in visited:
                distances[neighbour_node] = dist_from_parent + distances[curr_node]
                visited.add(neighbour_node)
                neighbour_node.set_parent(curr_node)
                neighbour_node.mark_as_visited()
                stack.append(neighbour_node)

        draw()

        if curr_node != start:
            curr_node.mark_as_finished()

    return False
