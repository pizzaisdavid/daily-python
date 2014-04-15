def occurrences(sequence, find):
    '''Return all indices of item in iterable as a list.'''
    indices = []
    for index, item in enumerate(sequence):
        if find == item:
            indices.append(index)
    return indices
