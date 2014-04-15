def occurrences(sequence, find):
    indices = []
    for index, element in enumerate(sequence):
        if find == element:
            indices.append(index)
    return indices
