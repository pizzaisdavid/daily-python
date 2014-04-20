def tree(width, trunk, leaf):
    count = width / 2
    TRUNK_WIDTH = 3
    for index in reversed(range(count + 1)):
        print index * ' ' + (width - 2 * index) * leaf
    print (count - 1) * ' ' + TRUNK_WIDTH * trunk

tree(7, '#', '*')
tree(13, '=', '+')
