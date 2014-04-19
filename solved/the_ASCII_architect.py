def main():
    def format_input(sequence):
        return list(sequence)
        
    def blank_house():
        house = []
        for index in range(20):
            house.append([])
        return house
                
    def build_house(sequence, house):
        numbers = '123456789'
        letters = 'abcdefghij'
        wall = '++--***...'
        for index, element in enumerate(sequence):
            spaces = 0
            s = wall[:letters.find(element) + 1]
            if sequence[index - 1] in numbers:
                s = int(sequence[index - 1]) * ' ' + s
            if element in letters:
                i = 0
                s = s + '                      '
            while i != len(house):
                house[i].append(s[i])
                i += 1
        return house

    def format_output(sequence):
        for element in reversed(sequence):
            print ''.join(element)
                
    input_string = 'j3f3e3e3d3d3c3cee3c3c3d3d3e3e3f3fjij3f3f3e3e3d3d3c3cee3c3c3d3d3e3e3fj'
    house = blank_house()
    input_list = format_input(input_string)
    house = build_house(input_string, house)
    format_output(house)

main()

