for element in range(1000, 10000):
    string = str(element)
    squared = (int(string[0:2]) + int(string[2:4])) ** 2
    if element == squared and set(string) == string:
        print element
