def occurrences(iterable, item):
    '''Find all occurrences of item in iterable and return them in a list.'''
    # return [i for i, x in enumerate(iterable) if x == item]
    indices = []
    for i, x in enumerate(iterable):
        if x == item:
            indices.append(i)
    return indices
