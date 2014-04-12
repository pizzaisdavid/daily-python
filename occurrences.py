def occurrences(iterable, find):
    '''Return all occurrences of find in iterable.'''
    # return [i for i, x in enumerate(iterable) if x == find]
    indices = []
    for i, x in enumerate(iterable):
        if x == find:
            indices.append(i)
    return indices
