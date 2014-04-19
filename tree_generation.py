def tree(width, trunk, leaf):
    space_count = width / 2
    TRUNK_COUNT = 3
    leaf_count = 1
    while space_count != 0:
        print space_count * ' ' + leaf_count * leaf
        leaf_count += 2
        space_count -= 1
    print ((width / 2) - 1) * ' ' + TRUNK_COUNT * trunk

tree(7, '#', '*')
tree(13, '=', '+')
