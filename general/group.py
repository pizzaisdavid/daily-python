def group(sequence):
    """
    Groups a list by a characteristic and puts it an a dictionary.
    """
    dictionary = {}
    for element in sequence:
        key = len(elment) # Characteristic we are grouping by.
        if key not in dictionary:
            dictonary[key] = []
        dictonary[key].append(element)
    return dictonary
