def tree(width, trunk, leaf):
    number_of_spaces = width / 2
    number_of_leafs = 1
    for count in reversed(number_of_spaces):
        print count * ' ' + number_of_leafs * leaf

tree(7, '#', '*')
