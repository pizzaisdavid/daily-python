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
        for element in sequence:
            if element in numbers:
                
        
    input_string = 'j3f3e3e3d3d3c3cee3c3c3d3d3e3e3f3fjij3f3f3e3e3d3d3c3cee3c3c3d3d3e3e3fj'
    house = blank_house()
    input_list = format_input(input_string)
    build_house(input_string, house)
        
