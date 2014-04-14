def contains_unique_elements(iterable):
    for index, element in enumerate(iterable):
        if element in iterable[:index] + iterable[index + 1:]:
            return False
    return True
