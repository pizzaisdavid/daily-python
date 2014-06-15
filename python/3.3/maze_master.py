def maze_master(filename):
    maze = setup(filename)
    player = Player(maze)
    WALL = '#'
    DEAD_END = 'B'
    EXPLORED = '*'
    UNEXPLORED = ' '
    EXIT = 'E'
    while player.is_in_maze():
        if player.at_dead_end(DEAD_END + WALL):
            player.mark_as(DEAD_END)
        else:
            player.mark_as(EXPLORED)
        player.move(UNEXPLORED, EXPLORED, EXIT)
    player.print_maze(DEAD_END)
    print('done')

def setup(filename):
    _, *maze = open(filename)
    grid = []
    for row in maze:
        line = list(row.strip())
        grid.append(line)
    return grid

class Player:
    def __init__(self, maze):
        self.maze = maze
        self.horizontal, self.vertical = Player.locate(self, 'S')

    def locate(self, symbol):
        horizontal, vertical = 0, 0
        for row in self.maze:
            horizontal = 0
            for cell in row:
                if cell == symbol:
                    return (horizontal, vertical)
                horizontal += 1
            vertical += 1

    def is_in_maze(self):
        EXIT = 'E'
        return self.maze[self.vertical][self.horizontal] != EXIT

    def at_dead_end(self, WALL):
        directions_blocked = 0
        DEAD_END = 3
        START = 'S'
        Player.get_surrounding_content(self)
        for cell in self.content:
            if cell in WALL:
                directions_blocked += 1
        if self.maze[self.vertical][self.horizontal] == START:
            return False
        return directions_blocked == DEAD_END

    def get_surrounding_content(self):
        content = []
        surrounding = [(self.vertical - 1, self.horizontal),
                       (self.vertical, self.horizontal + 1),
                       (self.vertical + 1, self.horizontal),
                       (self.vertical, self.horizontal - 1)
                       ]
        for x, y in surrounding:
            content.append(self.maze[x][y])
        self.content = content

    def mark_as(self, SYMBOL):
        self.maze[self.vertical][self.horizontal] = SYMBOL

    def move(self, UNEXPLORED, EXPLORED, EXIT):
        Player.get_dictonary_surrounding(self)
        if UNEXPLORED in self.adjacent.values():
            Player.move_to(self, UNEXPLORED)
        elif EXIT in self.adjacent.values():
            Player.move_to(self, EXIT)
        elif EXPLORED in self.adjacent.values():
            Player.move_to(self, EXPLORED)

    def get_dictonary_surrounding(self):
        DIRECTIONS = ['up', 'right', 'down', 'left']
        adjacent = {}
        for key, value in zip(DIRECTIONS, self.content):
            adjacent[key] = value
        self.adjacent = adjacent

    def move_to(self, SYMBOL):
        x, y = Player.get_direction(self, SYMBOL)
        self.horizontal += x
        self.vertical += y

    def get_direction(self, SYMBOL):
        directions = {'up': (0, -1),
                      'right': (1, 0),
                      'down': (0, 1),
                      'left': (-1, 0)
                      }
        for key in self.adjacent:
            if self.adjacent[key] == SYMBOL:
                return directions[key]

    def print_maze(self, DEAD_END):
        for row in self.maze:
            line = ''.join(row).replace(DEAD_END, ' ')
            print(line)

maze_master('maze.txt')
