def group(sequence):
    """Group by a characteristic and put them in a dictionary."""
    dictionary = {}
    for element in sequence:
        key = len(elment) # Characteristic we are grouping by.
        if key not in dictionary:
            dictionary[key] = []
        dictionary[key].append(element)
    return dictionary
