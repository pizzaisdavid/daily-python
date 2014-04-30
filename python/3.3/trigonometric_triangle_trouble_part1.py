def main():
    triangle = Triangle()
    print (triangle.a)
    
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
    adjacent = sides[0]
    opposite = sides[1]
    hypotenuse = sides[2]
    if hypotenuse == OPEN:
        hypotenuse = math.sqrt(adjacent**2 + opposite**2)
    elif adjacent == OPEN:
        adjacent = math.sqrt(hypotenuse**2 - opposite**2)
    else:
        opposite = math.sqrt(hypotenuse**2 - adjacent**2)
    return [adjacent, opposite, hypotenuse]
        
def solve_for_an_angle(angles):
    OPEN = 0
    unknown = 180
    for angle in angles:
        unknown -= angle
    angles[angles.index(OPEN)] = unknown
    return angles
    
print (solve_for_angle([34, 0, 90]))
