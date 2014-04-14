def occurrences(iterable, find):
    '''Return all indices of item in iterable as a list.'''
    indices = []
    for i, x in enumerate(iterable):
        if find == x:
            indices.append(i)
    return indices
