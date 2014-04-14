def contains_unique_elements(iterable):
    for i, x in enumerate(iterable):
        if x in iterable[:i] + iterable[i+1:]:
            return False
    return True
