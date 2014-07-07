def rotate(filename):
    DIMENSION, grid = setup(filename)
    TURNS = [90, 180, 270]
    for turn in TURNS:
        new_indices = translate(DIMENSION)
        grid = sync(grid, new_indices)
        output(DIMENSION, turn, grid)

def setup(filename):
    grid = []
    width, *array = open(filename)
    for row in array:
        grid.extend(row.split())
    return int(width), grid

def translate(DIMENSION):
    TOP_LEFT_CORNER = DIMENSION * (DIMENSION - 1)
    indices = []
    for horizontal in range(DIMENSION):
        shift = TOP_LEFT_CORNER + horizontal
        indices.extend(get_vertical_shifts(DIMENSION, shift))
    return indices

def get_vertical_shifts(DIMENSION, shift):
    shifts = []
    for vertical in range(DIMENSION):
        shifts.append(shift)
        shift -= DIMENSION
    return shifts

def sync(grid, indices):
    return [grid[index] for index in indices]

def output(DIMENSION, turn, grid):
    print(turn)
    for iterator in range(DIMENSION):
        print(get_row(DIMENSION, grid, iterator))
    print(' ')

def get_row(length, grid, iterator):
    return ' '.join(grid[iterator * length: (iterator + 1) * length])
          
rotate('rotate.txt')
