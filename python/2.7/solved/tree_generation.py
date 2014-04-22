def tree(width, trunk, leaf):
    count = width / 2
    TRUNK_WIDTH = 3
    for n in reversed(range(count + 1)):
        print n * ' ' + (width - 2 * n) * leaf
    print (count - 1) * ' ' + TRUNK_WIDTH * trunk

tree(7, '#', '*')
tree(13, '=', '+')
