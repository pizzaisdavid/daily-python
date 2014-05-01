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
    adjacent, opposite, hypotenuse = sides
    if hypotenuse == OPEN:
        hypotenuse = sqrt(adjacent**2 + opposite**2)
    elif adjacent == OPEN:
        adjacent = sqrt(hypotenuse**2 - opposite**2)
    else:
        opposite = sqrt(hypotenuse**2 - adjacent**2)
    return [adjacent, opposite, hypotenuse]
        
def solve_for_an_angle(angles):
    OPEN = 0
    unknown = 180
    for angle in angles:
        unknown -= angle
    angles[angles.index(OPEN)] = unknown
    return angles
    
print (pythagorean_theorem([3, 4, 0]))
