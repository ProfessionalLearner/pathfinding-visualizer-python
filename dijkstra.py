from queue import PriorityQueue
from typing import List
from node import GridNode
import pygame


def dijkstra_find_path(draw, grid: List[List[GridNode]], start: GridNode, end: GridNode, speed: int):
    distances = {node: float("inf") for row in grid for node in row}
    distances[start] = 0

    insertion_time = 0
    priority_queue = PriorityQueue()
    priority_queue.put((0, 0, start))
    visited = {start}

    clock = pygame.time.Clock()

    while not priority_queue.empty():
        for event in pygame.event.get():
            if event == pygame.QUIT:
                pygame.quit()

        curr_node = priority_queue.get()[2]
        visited.add(curr_node)

        clock.tick(speed)
        if curr_node == end:
            end.mark_as_end()
            return True

        for neighbour in curr_node.get_neighbours():
            neighbour_node = neighbour[0]
            dist_from_parent = neighbour[1]
            temp_distance = distances[curr_node] + dist_from_parent

            if temp_distance < distances[neighbour_node]:
                neighbour_node.set_parent(curr_node)
                distances[neighbour_node] = temp_distance
                if neighbour_node not in visited:
                    insertion_time += 1
                    priority_queue.put((distances[neighbour_node], insertion_time, neighbour_node))
                    visited.add(neighbour_node)
                    neighbour_node.mark_as_visited()

        draw()

        if curr_node != start:
            curr_node.mark_as_finished()

    return False
