    def rotate(filename):
        DIMENSION, grid = setup(filename)
        TURNS = [90, 180, 270]
        for turn in TURNS:
            indices = get_shifts(DIMENSION)
            grid = translate(grid, indices)
            output(DIMENSION, turn, grid)

    def setup(filename):
        grid = []
        n, *array = open(filename)
        for line in array:
            row = line.split()
            grid.extend(row)
        return int(n), grid

    def get_shifts(DIMENSION):
        LARGEST = DIMENSION * (DIMENSION - 1)
        indices = []
        for height in range(DIMENSION):
            shift = LARGEST + height
            for width in range(DIMENSION):
                indices.append(shift)
                shift -= DIMENSION
        return indices

    def translate(grid, indices):
        return [grid[index] for index in indices]

    def output(DIMENSION, turn, grid):
        print(turn)
        for width in range(DIMENSION):
            row = grid[width * DIMENSION: (width + 1) * DIMENSION]
            print(' '.join(row))
        print(' ')
        
            
    rotate('rotate.txt')
