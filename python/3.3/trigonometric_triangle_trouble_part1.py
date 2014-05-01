from math import sqrt

def main():
    triangle = Triangle()
    while triangle.is_solved == False:
        if triangle.unknown_side_count == 1:
            pythagorean_theorem(triangle.sides)
        elif triangle.unknown_side_count == 1:
            solve_for_an_angle(triangle.angles)
            
class Triangle:
    def __init__(self, *args):
        self.sides = [a, b, c]
        self.angles = [A, B, C]
        self.is_solved = False

def pythagorean_theorem(sides):
    OPEN = 0
    side1, side2, hypotenuse = sides
    if hypotenuse == OPEN:
        hypotenuse = sqrt(side1**2 + side2**2)
    elif side1 == OPEN:
        side1 = sqrt(hypotenuse**2 - side2**2)
    else:
        side2 = sqrt(hypotenuse**2 - side1**2)
    return [side1, side2, hypotenuse]
        
def solve_for_an_angle(angles):
    OPEN = 0
    unknown = 180
    for angle in angles:
        unknown -= angle
    angles[angles.index(OPEN)] = unknown
    return angles
    
print (pythagorean_theorem([3, 4, 0]))
