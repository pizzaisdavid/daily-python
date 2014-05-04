from math import sqrt, asin, acos, sin, cos, pi

def main():
    triangle = Triangle(a=3, b=4, C=90)
    while triangle.is_solved() == False:
        triangle = law_of_sines(triangle)
        triangle.sides = pythagorean_theorem(triangle.sides)
        triangle.angles = solve_for_an_angle(triangle.angles)
    return triangle.sides
            
class Triangle:
    def __init__(self, a=0, b=0, c=0, A=0, B=0, C=0):
        self.sides = [a, b, c]
        self.angles = [A, B, C]
        self.side_count = len(undefined_occurrences(self.sides))
        self.angle_count = len(undefined_occurrences(self.angles))
    
    def is_solved(self):
        UNKKNOWN = 0
        try:
            self.sides.index(UNKKNOWN)
            #self.angles.index(UNKKNOWN)
            return False
        except ValueError:
            return True

def undefined_occurrences(sequence, find=0):
     return [i for i, x in enumerate(sequence) if x == find]

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

def law_of_sines(triangle):
    angles = triangle.angles
    sides = triangle.sides
    angle_indices = undefined_occurrences(angles)
    side_indices = undefined_occurrences(sides)
    if len(angle_indices):
        angles = two_sides_and_angle(sides, angles, angle_indices, side_indices)
    #else:
    #    sides[]
        

def two_angles_and_side(sides, angles, angle_indices, side_indices):
    """Given two angles and a side, finds a second side."""
    i = side_indices
    unknown_index = other(angle_indices, i)
    #found = 

def two_sides_and_angle(sides, angles, angle_indices, side_indices):
    """Given two sides and an angle, finds a second angle."""
    i = angle_indices[0]
    unknown_index = other(side_indices, i)
    found = asin((sides[i] * sin(angles[unknown_index])) / sides[i])
    angles[unknown_index] = found
    return angles

def _sin(radians):
    """Radains to degrees"""
    return 180 * sin(radians) / pi

def other(sequence, find):
    for item in sequence:
        if item != find:
            return item




    
print _sin(90)
