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
    #             let v.parent = next
    #             add v to the end of discovered

    discovered = [start]

    while not end.visited and len(discovered) > 0:
        u = discovered.pop()

        u.visited = True

        if u == end:
            break

        for v in u.get_neighbours(board):
            if not v.visited:
                v.parent = u
                if v in discovered:
                    discovered.remove(v)
                discovered.append(v)

        yield u.get_path()

    if end.visited:
        yield end.get_path()
    else:
        yield []


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
    #             let v.parent = next
    #             add v to the end of discovered

    discovered = [start]

    while not end.visited and len(discovered) > 0:
        u = discovered.pop(0)

        u.visited = True

        if u == end:
            break

        for v in u.get_neighbours(board):
            if not v.visited and v not in discovered:
                v.parent = u
                discovered.append(v)

        yield u.get_path()

    if end.visited:
        yield end.get_path()
    else:
        yield []


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
    #             let v.parent = next
    #             let v.total_cost = new_cost
    #             add v to discovered

    discovered = {start}

    for row in board:
        for cell in row:
            cell.total_cost = float("inf")

    start.total_cost = 0

    while not end.visited and len(discovered) > 0:
        u = sorted(discovered, key=lambda c: c.total_cost)[0]
        discovered.remove(u)

        u.visited = True

        if u == end:
            break

        for v in u.get_neighbours(board):
            new_cost = u.total_cost + v.get_cost()
            if not v.visited and new_cost < v.total_cost:
                v.parent = u
                v.total_cost = new_cost
                discovered.add(v)

        yield u.get_path()

    if end.visited:
        yield end.get_path()
    else:
        yield []


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
    #             let v.parent = next
    #             let v.total_cost = new_cost
    #             let v.dist = u.dist + cost of moving to v
    #             add v to discovered

    discovered = {start}

    for row in board:
        for cell in row:
            cell.total_cost = float("inf")
            cell.dist = float("inf")

            cell.heuristic = math.sqrt((cell.x - end.x) ** 2 + (cell.y - end.y) ** 2)

    start.total_cost = start.heuristic
    start.dist = 0

    while not end.visited and len(discovered) > 0:
        u = sorted(discovered, key=lambda c: c.total_cost)[0]
        discovered.remove(u)

        u.visited = True

        if u == end:
            break

        for v in u.get_neighbours(board):
            new_cost = u.dist + v.get_cost() + v.heuristic
            if not v.visited and new_cost < v.total_cost:
                v.parent = u
                v.total_cost = new_cost
                v.dist = u.dist + v.get_cost()
                discovered.add(v)

        yield u.get_path()

    if end.visited:
        yield end.get_path()
    else:
        yield []
