def occurrences(iterable, find):
    # return [i for i, x in enumerate(iterable) if x == find]
    indices = []
    for i, x in enumerate(iterable):
        if x == find:
            indices.append(i)
    return indices
