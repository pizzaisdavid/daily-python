from math import sqrt
"""
ADD
-SAS
-ASA
"""
def main():
    triangle = Triangle(a=3, b=4)
    while triangle.is_solved() == False:
        if triangle.unknown_side_count == 1:
            triangle.sides = pythagorean_theorem(triangle.sides)
        #elif triangle.is_unknown_side_count == 1:
        #    triangle.angles = solve_for_an_angle(triangle.angles)
    return triangle.sides
            
class Triangle:
    def __init__(self, a=0, b=0, c=0, A=0, B=0, C=0):
        self.sides = [a, b, c]
        self.angles = [A, B, C]
        self.unknown_side_count = number_of_occurrences(self.sides)
        self.unknown_angle_count = number_of_occurrences(self.angles)
    
    def is_solved(self):
        UNKKNOWN = 0
        try:
            self.sides.index(UNKKNOWN)
            #self.angles.index(UNKKNOWN)
            return False
        except ValueError:
            return True

def number_of_occurrences(sequence, find=0):
     return len([i for i, x in enumerate(sequence) if x == find])

def pythagorean_theorem(sides):
    side1, side2, hypotenuse = sides
    if is_unknown(hypotenuse):
        found_side = hypotenuse_from_sides(side1, side2)
    else:
        found_side = solve_for_side(side1, side2, hypotenuse)
    return insert_value(sides, found_side)

def is_unknown(item):
    UNKKNOWN = 0
    return item == UNKKNOWN

def hypotenuse_from_sides(side1, side2):
    return sqrt(side1**2 + side2**2)

def solve_for_side(side1, side2, hypotenuse):
    known_side = side2
    if is_unknown(side2):
        known_side = side1
    return sqrt(hypotenuse**2 - known_side**2)

def insert_value(sequence, value):
    REPLACE = 0
    sequence[sequence.index(REPLACE)] = value
    return sequence

def solve_for_an_angle(angles):
    found_angle = 180
    for angle in angles:
        found_angle -= angle
    return insert_value(angles, found_angle)
    
print main()
