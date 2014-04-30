def main():
    triangle = Triangle()
    print (triangle.a)
    
    while triangle.is_solved == False:
        if triangle.unknown_side_count == 1:
            pythagorean_theorem()
        elif triangle.unknown_side_count == 1:
            solve_for_an_angle(triangle.angle)
            
class Triangle:
    def __init__(self, *args):
        self.sides = [a, b, c]
        self.angles = [A, B, C]
        self.is_solved = False

def pythagorean_theorem(sides):
    square_root = math.sqrt()
    OPEN = 0
    if sides[2] == OPEN:
        sides[2] = square_root(side[0]**2 + side[1]**2)
    elif:

    return sides
        
def solve_for_an_angle(angles):
    OPEN = 0
    unknown = 180
    for angle in angles:
        unknown -= angle
    angles[angles.index(OPEN)] = unknown
    return angles
    
print (solve_for_angle([34, 0, 90]))
