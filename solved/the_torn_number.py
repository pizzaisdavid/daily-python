for element in range(1000, 10000):
    string = str(element)
    combined = int(string[0:2]) + int(string[2:4])
    if element == combined ** 2 and len(set(string)) == len(string):
        print element
