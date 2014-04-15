def unique(sequence):
    for index, element in enumerate(sequence):
        if element in sequence[index + 1:]:
            return False
    return True
