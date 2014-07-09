def setup(filename):
    grid = []
    with open(filename) as file:
        length, *datas = file
        for data in datas:
            grid.extend(data.split())
    return int(length), grid
            
