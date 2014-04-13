def longest(iterable):
    longest = ''
    for item in iterable:
        if len(longest) < len(item):
            longest = item
    return longest
