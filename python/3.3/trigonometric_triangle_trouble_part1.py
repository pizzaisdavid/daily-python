def main():
    triangle = Triangle()
    print (triangle.a)
    
    while triangle.is_solved == False:
        if triangle.unknown_side_count == 1:
            pythagorean_theorem()
        elif triangle.unknown_side_count == 1:
            solve_for_angle(triangle.angle)
            
class Triangle:
    __init__(self, *args):
        self.sides = [a, b, c]
        self.angles = [A, B, C]
        self.is_solved = False
        
def solve_for_angle(angles):
    unknown_index = occurrences(angles, 0)
    unknown_angle = 180
    for angle in angles:
        unknown_angle -= angle
    angles[unknown_index] = unknown_angle
    return angles
    
def occurrences(sequence, find):
    return [i for i, x in enumerate(sequence) if x == find]
    
main()
