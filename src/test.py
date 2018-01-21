import Queue

def num_moves(grid, pos):
    to_try = Queue.PriorityQueue()
    to_try.put((0, pos))
    while not to_try.empty():
        num, (x,y) = to_try.get()
        if 0 <= x < 8 and 0 <= y < 8 and grid[x][y] == -1:
            grid[x][y] = num
            to_try.put((num + 1, (x-2, y+1)))
            to_try.put((num + 1, (x-2, y-1)))
            to_try.put((num + 1, (x+2, y+1)))
            to_try.put((num + 1, (x+2, y-1)))
            to_try.put((num + 1, (x-1, y+2)))
            to_try.put((num + 1, (x-1, y-2)))
            to_try.put((num + 1, (x+1, y+2)))
            to_try.put((num + 1, (x+1, y-2)))
    return grid


def print_grid(grid):
    for row in grid:
        print(row)

def standard_grid():
    return [[-1] * 8 for _ in range(8)]

board = standard_grid()
board[0][3] = 9
board[2][3] = 9
board[3][0] = 9
board[3][2] = 9

print_grid(num_moves(board, (1,1)))