import pygame
import pathfinding
from cell import Cell

# keybinds
# left mouse button              : draw wall
# right mouse button             : erase wall
# left alt + left mouse button   : draw mud
# left shift + left mouse button : set start cell
# left ctrl + left mouse button  : set end cell
# right shift                    : save board
# right ctrl                     : load board
# enter                          : start/stop pathfinding

# configurations
CELL_SIZE = 40
WIDTH = 20
HEIGHT = 20

# pathfinding settings
pathfinding_algo = pathfinding.depth_first_search
pathfinding_fps = 20

# create board and other variables
board = [[Cell(x, y) for x in range(WIDTH)] for y in range(HEIGHT)]
start_pos = (0, 0)
end_pos = (WIDTH - 1, HEIGHT - 1)
drawing = True

board[start_pos[1]][start_pos[0]].type = Cell.START_TYPE
board[end_pos[1]][end_pos[0]].type = Cell.END_TYPE

# pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH * CELL_SIZE, HEIGHT * CELL_SIZE))

# main loop
while True:
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                drawing = not drawing
                for row in board:
                    for cell in row:
                        cell.reset_pathfinding_data()

                if not drawing:
                    path_generator = pathfinding_algo(board, board[start_pos[1]][start_pos[0]],
                                                      board[end_pos[1]][end_pos[0]])
            elif drawing:
                if event.key == pygame.K_DELETE:
                    for row in board:
                        for cell in row:
                            cell.type = Cell.EMPTY
                elif event.key == pygame.K_RSHIFT:
                    with open('board.txt', 'w') as f:
                        for row in board:
                            for cell in row:
                                f.write(str(cell.type))
                            f.write('\n')
                elif event.key == pygame.K_RCTRL:
                    with open('board.txt', 'r') as f:
                        for y, row in enumerate(f.readlines()):
                            row = row.strip()
                            for x, cell_type in enumerate(row):
                                board[y][x].type = int(cell_type)
                                if board[y][x].type == Cell.START_TYPE:
                                    start_pos = (x, y)
                                elif board[y][x].type == Cell.END_TYPE:
                                    end_pos = (x, y)
    # update
    if drawing:
        def get_mouse_cell_pos():
            x, y = pygame.mouse.get_pos()
            x = x // CELL_SIZE
            y = y // CELL_SIZE

            if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
                return None
            return x, y

        if pygame.mouse.get_pressed()[0]:
            cell_pos = get_mouse_cell_pos()
            if cell_pos is not None and cell_pos != start_pos and cell_pos != end_pos:
                x, y = cell_pos
                if pygame.key.get_pressed()[pygame.K_LSHIFT]:
                    board[start_pos[1]][start_pos[0]].type = Cell.EMPTY
                    start_pos = (x, y)
                    board[start_pos[1]][start_pos[0]].type = Cell.START_TYPE
                elif pygame.key.get_pressed()[pygame.K_LCTRL]:
                    board[end_pos[1]][end_pos[0]].type = Cell.EMPTY
                    end_pos = (x, y)
                    board[end_pos[1]][end_pos[0]].type = Cell.END_TYPE
                elif pygame.key.get_pressed()[pygame.K_LALT]:
                    board[y][x].type = Cell.MUD_TYPE
                else:
                    board[y][x].type = Cell.WALL_TYPE
        elif pygame.mouse.get_pressed()[2]:
            cell_pos = get_mouse_cell_pos()
            if cell_pos is not None and cell_pos != start_pos and cell_pos != end_pos:
                x, y = cell_pos
                board[y][x].type = Cell.EMPTY

        # draw screen
        screen.fill((255, 255, 255))
        for row in board:
            for cell in row:
                cell.draw(screen, CELL_SIZE)
    else:
        # pathfinding
        try:
            path = next(path_generator)

            # draw screen
            screen.fill((255, 255, 255))
            for row in board:
                for cell in row:
                    cell.draw(screen, CELL_SIZE)

            for cell in path:
                if cell.type == Cell.MUD_TYPE:
                    cell.draw(screen, CELL_SIZE, (0, 0, 192))
                else:
                    cell.draw(screen, CELL_SIZE, (0, 0, 255))
        except StopIteration:
            pass

        # delay
        delay = 1000 // pathfinding_fps
        start = pygame.time.get_ticks()
        while pygame.time.get_ticks() - start < delay:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        drawing = not drawing
                        for row in board:
                            for cell in row:
                                cell.reset_pathfinding_data()
            pygame.display.update()

    pygame.display.update()
