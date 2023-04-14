from __future__ import annotations
from typing import Union
import pygame


class Cell:
    EMPTY = 0
    WALL_TYPE = 1
    MUD_TYPE = 2
    START_TYPE = 3
    END_TYPE = 4

    def __init__(self, x, y):
        # basic info
        self.x = x
        self.y = y
        self.type = self.EMPTY

        # pathfinding data
        self.total_cost = float('inf')
        self.heuristic = float('inf')
        self.dist = float('inf')
        self.visited = False
        self.parent = None

    # reset pathfinding data
    def reset_pathfinding_data(self):
        self.total_cost = float('inf')
        self.heuristic = float('inf')
        self.dist = float('inf')
        self.visited = False
        self.parent = None

    # get a list of neighbours
    def get_neighbours(self, board: list[list[Cell]]) -> list[Cell]:
        neighbour_pos = [
            (self.x - 1, self.y),
            (self.x, self.y - 1),
            (self.x + 1, self.y),
            (self.x, self.y + 1)
        ]

        return [board[pos[1]][pos[0]] for pos in neighbour_pos if
                0 <= pos[0] < len(board[0]) and 0 <= pos[1] < len(board) and board[pos[1]][
                    pos[0]].type != self.WALL_TYPE]

    # get path
    def get_path(self) -> list[Cell]:
        path = []
        current = self
        while current is not None:
            path.append(current)
            current = current.parent
        path.reverse()
        return path

    # get the cost of moving to this cell
    def get_cost(self) -> int:
        if self.type == self.MUD_TYPE:
            return 5
        return 1

    # draw this cell on screen
    def draw(self, screen: pygame.Surface, cell_size: int, color: Union[tuple[int, int, int], None] = None):
        rect = (self.x * cell_size, self.y * cell_size, cell_size, cell_size)

        if color is not None:
            pygame.draw.rect(screen, color, rect)
            return

        # draw the basic color
        if self.type == Cell.WALL_TYPE:
            pygame.draw.rect(screen, (0, 0, 0), rect)
        elif self.type == Cell.MUD_TYPE:
            pygame.draw.rect(screen, (128, 128, 128), rect)
        elif self.type == Cell.START_TYPE:
            pygame.draw.rect(screen, (0, 255, 0), rect)
        elif self.type == Cell.END_TYPE:
            pygame.draw.rect(screen, (255, 0, 0), rect)

        # draw the pathfinding data
        if self.visited:
            if self.type == Cell.MUD_TYPE:
                pygame.draw.rect(screen, (192, 192, 0), rect)
            else:
                pygame.draw.rect(screen, (255, 255, 0), rect)
