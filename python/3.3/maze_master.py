def maze_master(filename):
    maze = setup(filename)
    position = Position(maze)
    labyrinth = Labyrinth(maze)
    DEAD_END = 'd'
    EXPLORED = '.'
    while position.is_in_maze():
        if labyrinth.is_dead_end(position):
            labyrinth.mark(position, DEAD_END)
        else:
            labyrinth.mark(position, EXPLORED)
        position.move(labyrinth.maze)
        print(labyrinth.maze)

def setup(filename):
    _, *maze = open(filename)
    grid = []
    for row in maze:
        grid.append(list(row.strip()))
    return grid

class Position:
    def __init__(self, maze):
        self.maze = maze
        self.EXIT = locate(maze, 'E')
        self.horizontal, self.vertical = locate(maze, 'S')
        print(self.horizontal, self.vertical)

    def is_in_maze(self):
        return self.EXIT != (self.x, self.y)

    def move(self, maze):
        Position.get_surrounding(self)
        UNEXPLORED = ' '
        EXPLORED = '.'
        if UNEXPLORED in self.adjacent:
            Position.move_to(self, UNEXPLORED)
        elif EXPLORED in self.adjacent.values():
            Position.move_to(self, EXPLORED)
        else:
            r = input('d')

    def get_surrounding(self):
        adjacent = {}
        x, y = self.x, self.y
        first_entry = [x + 1, x, x - 1, x]
        second_entry = [y, y + 1, y, y - 1]
        DIRECTIONS = ['up', 'horizontal', 'vertical', 'left']
        for direction, x, y in zip(DIRECTIONS, first_entry, second_entry):
            adjacent[direction] = self.maze[x][y]
        self.adjacent = adjacent

    def move_to(self, SYMBOL):
        x, y = Position.get_direction(self, SYMBOL)
        self.x = self.x + x
        self.y = self.y + y

    def get_direction(self, SYMBOL):
        directions = {'up' : (0, -1),
                      'horizontal' : (1, 0),
                      'vertical' : (0, 1),
                      'left' : (-1, 0)
                      }
        for key in self.adjacent:
            if self.adjacent[key] == SYMBOL:
                return directions[key]

def locate(grid, symbol):
    horizontal, vertical = 0, 0
    for row in grid:
        horizontal = 0
        for cell in row:
            if cell == symbol:
                return (horizontal, vertical)
            horizontal += 1
        vertical += 1

class Labyrinth:
    def __init__(self, maze):
        self.maze = maze

    def is_dead_end(self, position):
        WALL = ['#', 'd']
        START = 'S'
        DEAD_END = 3
        surrounding = [(position.x + 1, position.y),
                       (position.x, position.y + 1),
                       (position.x - 1, position.y),
                       (position.x, position.y - 1)
                       ]
        count = 0
        for x, y in surrounding:
            if self.maze[x][y] in WALL:
                count += 1
        return count == DEAD_END

    def mark(self, position, symbol):
        self.maze[position.x][position.y] = symbol

maze_master('maze.txt')
