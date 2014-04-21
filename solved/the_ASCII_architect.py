def main(blueprint):
    def print_output(building):
        i = len(building[0])
        while i > 0:
            row = ''
            i -= 1
            for column in building:
                row += column[i]
            print row

    def structure(blueprint):
        ROW_LENGTH = 22
        pattern = '++--***...'
        building = []
        letters = 'abcdefghij'
        pads = 0
        for element in blueprint:
            if element.isdigit():
                pads = int(element)
            else:
                i = letters.find(element)
                column = ' ' * pads + pattern[:i + 1] + ' ' * (ROW_LENGTH - pads - i)
                building.append(column)
                pads = 0
        return building

    print_output(structure(blueprint))

main('j3f3e3e3d3d3c3cee3c3c3d3d3e3e3f3fjij3f3f3e3e3d3d3c3cee3c3c3d3d3e3e3fj')
