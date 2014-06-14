def maze_master(filename):
    maze = setup(filename)
    position = Position(maze)
    labyrinth = Labyrinth(maze)
    while position.is_in_maze():
        if labyrinth.is_dead_end(position):
            labyrinth.mark_as_dead_end(position)
        else:
            labyrinth.mark_as_explored(position)
        position.move(labyrinth.maze)
        
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
        self.x, self.y = locate(maze, 'S')

    def is_in_maze(self):
        return self.EXIT != (self.x, self.y)

    def move(self, maze):
        Position.get_adjacent(self)

    def get_adjacent(self):
        adjacent = []
        Position.get_surrounding(self)
        self.DIRECTIONS = ['up', 'right', 'down', 'left']
        for key, value in zip(self.DIRECTIONS, self.content):
            adjacent[key] = value
        self.adjacent = adjacent

    def get_surrounding(self):
        x = self.x
        y = self.y
        content = []
        surrounding = [(x + 1, y),
                       (x, y + 1),
                       (x - 1, y),
                       (x, y - 1)
                       ]
        for x, y in surrounding:
            content.append(self.maze[x][y])
        self.content = content

def locate(grid, symbol):
    x, y = 0, 0
    for row in grid:
        x = 0
        for cell in row:
            if cell == symbol:
                return x, y
            x += 1
        y += 1

class Labyrinth:
    def __init__(self, maze):
        self.maze = maze

    def is_dead_end(self, position):
        WALL = ['#', False]
        DEAD_END = 3
        surrounding = ([position.x + 1, position.y],
                       [position.x, position.y + 1],
                       [position.x - 1, position.y],
                       [position.x, position.y - 1]
                       ) 
        count = 0
        for x, y in surrounding:
            if self.maze[x][y] in WALL:
                count += 1
        return count == DEAD_END

    def mark_as_dead_end(self, position):
        DEAD_END = False
        Labyrinth.mark(self, position, DEAD_END)

    def mark_as_explored(self, position):
        EXPLORED = '.'
        Labyrinth.mark(self, position, EXPLORED)

    def mark(self, position, assignment):
        self.maze[position.x][position.y] = assignment
        
        
    
maze_master('maze.txt')
