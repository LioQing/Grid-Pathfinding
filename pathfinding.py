import math

from cell import Cell
from typing import Generator


def depth_first_search(board: list[list[Cell]], start: Cell, end: Cell) -> Generator[list[Cell], None, None]:
    # let discovered = a set containing start cell
    #
    # while end cell is not visited and discovered is not empty:
    #     let u = pop the latest cell from discovered
    #
    #     u.visited = True
    #
    #     if u is end cell:
    #         return path along u.parent
    #
    #     for each neighbor v of u:
    #         if v is not a wall and not visited:
    #             let v.parent = u
    #             add v to the end of discovered

    pass


def breadth_first_search(board: list[list[Cell]], start: Cell, end: Cell) -> Generator[list[Cell], None, None]:
    # let discovered = a set containing start cell
    #
    # while end cell is not visited and discovered is not empty
    #     let u = pop the earliest cell from discovered
    #
    #     u.visited = True
    #
    #     if u is end cell:
    #         return path along u.parent
    #
    #     for each neighbor v of u:
    #         if v is not a wall and not visited:
    #             let v.parent = u
    #             add v to the end of discovered

    pass


def dijkstra(board: list[list[Cell]], start: Cell, end: Cell) -> Generator[list[Cell], None, None]:
    # let discovered = a sorted set containing start cell
    # set all cells' total cost to infinity
    # set start cell's total cost to 0
    #
    # while end cell is not visited and discovered is not empty:
    #     let u = pop the lowest total cost cell from discovered
    #
    #     u.visited = True
    #
    #     if u is end cell:
    #         return path along u.parent
    #
    #     for each neighbor v of u:
    #         let new_cost = u.total_cost + cost of moving to v
    #         if v is not visited and new_cost < v.total_cost:
    #             let v.parent = u
    #             let v.total_cost = new_cost
    #             add v to discovered

    pass


def a_star(board: list[list[Cell]], start: Cell, end: Cell) -> Generator[list[Cell], None, None]:
    # let discovered = a sorted set containing start cell
    # set all cells' total cost to infinity
    # set all cells' dist to infinity
    #
    # set all cells' heuristic to the euclidean distance to the end cell
    #
    # set start cell's total cost to its heuristic
    # set start cell's dist to 0
    #
    # while end cell is not visited and discovered is not empty:
    #     let u = pop the lowest total cost cell from discovered
    #
    #     u.visited = True
    #
    #     if u is end cell:
    #         return path along u.parent
    #
    #     for each neighbor v of u:
    #         let new_cost = u.total_cost + cost of moving to v + v's heuristic
    #         if v is not visited and new_cost < v.total_cost:
    #             let v.parent = u
    #             let v.total_cost = new_cost
    #             let v.dist = u.dist + cost of moving to v
    #             add v to discovered

    pass
