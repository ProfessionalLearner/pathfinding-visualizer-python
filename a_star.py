from queue import PriorityQueue
from typing import List
from node import GridNode
from heuristics import get_manhattan_distance as h
import pygame


def a_star_find_path(draw, grid: List[List[GridNode]], start: GridNode, end: GridNode, speed: int):
    node_width = start.width
    node_height = start.height

    insertion_time = 0

    priority_queue = PriorityQueue()
    priority_queue.put((0, insertion_time, start))

    g_scores = {node: float("inf") for row in grid for node in row}
    g_scores[start] = 0

    f_score = {node: float("inf") for row in grid for node in row}
    f_score[start] = h(start.get_position(), end.get_position(), node_width, node_height)

    nodes_in_queue = {start}

    clock = pygame.time.Clock()

    while not priority_queue.empty():
        for event in pygame.event.get():
            if event == pygame.QUIT:
                pygame.quit()

        curr_node = priority_queue.get()[2]
        nodes_in_queue.remove(curr_node)

        if curr_node == end:
            end.mark_as_end()
            return True

        clock.tick(speed)
        for neighbour in curr_node.get_neighbours():
            neighbour_node = neighbour[0]
            dist_from_parent = neighbour[1]
            temp_g_score = g_scores[curr_node] + dist_from_parent

            if temp_g_score < g_scores[neighbour_node]:
                neighbour_node.set_parent(curr_node)
                g_scores[neighbour_node] = temp_g_score
                f_score[neighbour_node] = temp_g_score + h(neighbour_node.get_position(), end.get_position(),
                                                           node_width, node_height)
                if neighbour_node not in nodes_in_queue:
                    insertion_time += 1
                    priority_queue.put((f_score[neighbour_node], insertion_time, neighbour_node))
                    nodes_in_queue.add(neighbour_node)
                    neighbour_node.mark_as_visited()

        draw()

        if curr_node != start:
            curr_node.mark_as_finished()

    return False
