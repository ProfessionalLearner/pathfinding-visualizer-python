from typing import List
from node import GridNode
from collections import deque
import pygame


def breadth_first_search_find_path(draw, grid: List[List[GridNode]], start: GridNode, end: GridNode, speed: int):
    distances = {node: float("inf") for row in grid for node in row}
    distances[start] = 0

    visited = {start}

    q = deque()
    q.appendleft(start)

    clock = pygame.time.Clock()

    while q:
        for event in pygame.event.get():
            if event == pygame.QUIT:
                pygame.quit()

        curr_node = q.pop()

        clock.tick(speed)
        if curr_node == end:
            end.mark_as_end()
            return True

        for neighbour in curr_node.get_neighbours():
            neighbour_node = neighbour[0]
            dist_from_parent = neighbour[1]

            if neighbour_node not in visited:
                visited.add(neighbour_node)
                distances[neighbour_node] = distances[curr_node] + dist_from_parent
                neighbour_node.set_parent(curr_node)
                q.appendleft(neighbour_node)
                neighbour_node.mark_as_visited()

        draw()

        if curr_node != start:
            curr_node.mark_as_finished()

    return False

