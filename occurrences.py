def occurrences(iterable, item):
    '''Return all indices of item in iterable as a list.'''
    # return [i for i, x in enumerate(iterable) if x == item]
    indices = []
    for i, x in enumerate(iterable):
        if x == item:
            indices.append(i)
    return indices
