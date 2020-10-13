import pygame
from algorithms import ALGORITHMS, ALGORITHMS_LIST, path_finding_algorithm
from node import GridNode
from colors import ColorRGB
from typing import Tuple, List
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import tkinter.font as tkFont
from text_for_application import *
from speed import ExecutionSpeed
import os

WIDTH = 800
HEIGHT = 600  # 4:3 aspect ratio
MENU_WIDTH = 200
root = tk.Tk()
root.title("Pathfinding Visualizer")
root.resizable(False, False)

embed = tk.Frame(root, width=WIDTH, height=HEIGHT)  # creates embed frame for pygame window
embed.pack(side=RIGHT)
embed.pack_propagate(0)

buttons_win = tk.Frame(root, width=MENU_WIDTH, height=HEIGHT)
buttons_win.pack(side=RIGHT)
buttons_win.pack_propagate(0)

os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'windib'

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Path finding vizualization")
pygame.display.init()
pygame.display.update()


def make_grid(rows: int, cols: int, width: int, height: int) -> List[List[GridNode]]:
    grid = []
    node_width = width // cols
    node_height = height // rows
    for i in range(rows):
        grid.append([])
        for j in range(cols):
            node = GridNode(i, j, node_width, node_height,
                            rows, cols)
            grid[i].append(node)
    return grid


def draw_grid(win, rows: int, cols: int, width: int, height: 1):
    node_width = width // cols
    node_height = height // rows
    for i in range(rows):
        pygame.draw.line(win, ColorRGB.GRAY.value, (0, i * node_height),  # horizontal lines
                         (width, i * node_height))
        for j in range(cols):
            pygame.draw.line(win, ColorRGB.GRAY.value, (j * node_width, 0),  # vertical lines
                             (j * node_width, height))


def draw(win, grid: List[List[GridNode]], rows: int, cols: int,
         width: int, height: int):
    win.fill(ColorRGB.WHITE.value)

    for row in grid:
        for node in row:
            node.draw(win)

    draw_grid(win, rows, cols, width, height)
    pygame.display.update()


def get_click_pos(pos: Tuple[int, int], rows: int, cols: int, width: int, height: int) -> Tuple[int, int]:
    node_width = width // cols
    node_height = height // rows
    x, y = pos

    col = x // node_width
    row = y // node_height

    return row, col


def start_stop_algorithm():
    pass


def main(win, width: int, height: int):
    ROWS = 30
    COLS = 40

    grid = [make_grid(ROWS, COLS, width, height)]

    start_node = [None]
    end_node = [None]

    path_finding_algorithm_type = None
    allow_diagonals = False
    algorithm_speed = ExecutionSpeed.FAST

    global run
    run = True

    # Legend for nodes for GUI
    tk.Label(buttons_win,
             text="Legend:"
             ).pack(anchor=W)

    canvas = tk.Canvas(root, width=6, height=6, bg=ColorRGB.ORANGE.from_rgb())
    canvas.pack(pady=0)
    canvas.place(x=8, y=27 + 1)

    canvas = tk.Canvas(root, width=6, height=6, bg=ColorRGB.BLUE.from_rgb())
    canvas.pack(pady=0)
    canvas.place(x=8, y=46 + 4)

    canvas = tk.Canvas(root, width=6, height=6, bg=ColorRGB.LIME.from_rgb())
    canvas.pack(pady=0)
    canvas.place(x=8, y=66 + 6)

    canvas = tk.Canvas(root, width=6, height=6, bg=ColorRGB.RED.from_rgb())
    canvas.pack(pady=0)
    canvas.place(x=8, y=84 + 6)

    canvas = tk.Canvas(root, width=6, height=6, bg=ColorRGB.PURPLE.from_rgb())
    canvas.pack(pady=0)
    canvas.place(x=8, y=103 + 9)

    canvas = tk.Canvas(root, width=6, height=6, bg=ColorRGB.BLACK.from_rgb())
    canvas.pack(pady=0)
    canvas.place(x=8, y=122 + 9)

    tk.Label(buttons_win,
             text="""          start""",
             anchor='w').pack(fill=BOTH)
    tk.Label(buttons_win,
             text="""          end""",
             anchor='w').pack(fill=BOTH)
    tk.Label(buttons_win,
             text="""          visited""",
             anchor='w').pack(fill=BOTH)
    tk.Label(buttons_win,
             text="""          explored""",
             anchor='w').pack(fill=BOTH)
    tk.Label(buttons_win,
             text="""          path""",
             anchor='w').pack(fill=BOTH)
    tk.Label(buttons_win,
             text="""          barrier""",
             anchor='w').pack(fill=BOTH)

    tk.Label(buttons_win,
             text="""Choose node (left click to add 
    and right click to remove node):"""
             ).pack(anchor=W)

    node_selected = StringVar()
    node_selected.set("Start")

    for node_type in ["Start", "End", "Barrier"]:
        tk.Radiobutton(buttons_win,
                       text=node_type,
                       padx=20,
                       variable=node_selected,
                       value=node_type).pack(anchor=W)

    tk.Label(buttons_win,
             text="Choose algorithm:",
             ).pack(anchor=W)

    algorithm_name = StringVar()
    algorithm_name.set("A*")

    for algorithm in ALGORITHMS_LIST:
        tk.Radiobutton(buttons_win,
                       text=algorithm,
                       padx=20,
                       variable=algorithm_name,
                       value=algorithm).pack(anchor=W)

    tk.Label(buttons_win,
             text="Choose algorithm execution speed:",
             ).pack(anchor=W)

    algo_speed = StringVar()
    algo_speed.set("Very Fast")

    for speed in ExecutionSpeed:
        tk.Radiobutton(buttons_win,
                       text=speed.__str__(),
                       padx=20,
                       variable=algo_speed,
                       value=speed.__str__()).pack(anchor=W)

    can_move_diagonally = IntVar()

    Checkbutton(buttons_win,
                text="Allow diagonal movement",
                variable=can_move_diagonally,
                ).pack(anchor=W)

    def start_button():
        if path_finding_algorithm_type is not None and start_node[0] is not None and end_node[0] is not None:
            for row in grid[0]:
                for node in row:
                    node.update_neighbours(grid[0], allow_diagonals)

            path_finding_algorithm(lambda: draw(win, grid[0], ROWS, COLS, width, height), grid[0], start_node[0],
                                   end_node[0], algorithm_speed.value, path_finding_algorithm_type)

    button_start = tk.Button(buttons_win,
                             text="Start",
                             font=tkFont.Font(size=11),
                             borderwidth=3,
                             width=10,
                             command=lambda: start_button())

    button_start.pack(side=LEFT, padx=(0, 5), pady=(1, 0))

    def reset_grid(start, end, grid_nodes):
        start[0] = None
        end[0] = None
        grid_nodes[0] = make_grid(ROWS, COLS, width, height)

    button_reset = tk.Button(buttons_win,
                             text="Reset",
                             font=tkFont.Font(size=11),
                             borderwidth=3,
                             width=10,
                             command=lambda: reset_grid(start_node, end_node, grid))

    button_reset.pack(side=LEFT, padx=(0, 0), pady=(1, 0))

    def on_closing():
        global run
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            run = False
            root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)

    messagebox.showinfo(TITLE, WELCOME_MESSAGE)

    while run:
        draw(win, grid[0], ROWS, COLS, width, height)
        root.update()

        path_finding_algorithm_type = algorithm_name.get()
        algorithm_speed = ExecutionSpeed.from_str(algo_speed.get())
        allow_diagonals = can_move_diagonally.get()
        node_type = node_selected.get()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if any(pygame.mouse.get_pressed()):
                pos_click = pygame.mouse.get_pos()
                row, col = get_click_pos(pos_click, ROWS, COLS, width, height)
                node = grid[0][row][col]
                if pygame.mouse.get_pressed()[0]:  # left mouse button
                    if node_type == "Start" and not start_node[0] and node != end_node[0] and not node.is_barrier():
                        start_node[0] = node
                        start_node[0].reset_node()
                        start_node[0].mark_as_start()

                    elif node_type == "End" and not end_node[0] and node != start_node[0] and not node.is_barrier():
                        end_node[0] = node
                        end_node[0].reset_node()
                        end_node[0].mark_as_end()

                    elif node_type == "Barrier" and node != end_node[0] and node != start_node[0]:
                        node.reset_node()
                        node.mark_as_barrier()

                elif pygame.mouse.get_pressed()[2]:  # right mouse button
                    if node_type == "Start" and start_node[0] is not None and node == start_node[0]:
                        node.reset_node()
                        start_node[0] = None

                    elif node_type == "End" and end_node[0] is not None and node == end_node[0]:
                        node.reset_node()
                        end_node[0] = None

                    elif node_type == "Barrier" and node.is_barrier():
                        node.reset_node()

    pygame.quit()


if __name__ == "__main__":
    main(WIN, WIDTH, HEIGHT)
