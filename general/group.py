def group(sequence):
    """Group by a characteristic and put them in a dictionary."""
    dictionary = {}
    for element in sequence:
        key = len(elment) # Characteristic we are grouping by.
        if key not in dictionary:
            dictonary[key] = []
        dictonary[key].append(element)
    return dictonary
