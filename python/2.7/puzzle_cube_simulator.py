def format_input():
    notation = "U2 R' D2 R F L' U2 R".split(' ')
    return notation

def create():
    cube = {'B':'w', 'U':'y', 'F':'r', 'R':'g', 'B':'o', 'L':'b'}
    for key in cube.keys():
        cube[key] = [cube[key]] * 9
    return cube

def rotate(face, transfer):
    new = [' '] * 9
    for index, element in enumerate(transfer):
        new[index] = face[element]
    return new

def rotate_90(face):
    transfer = [6, 3, 0, 7, 4, 1, 8, 5, 2]
    return rotate(face, transfer)

def rotate_180(face):
    transfer = [8, 7, 6, 5, 4, 3, 2, 1, 0]
    return rotate(face, transfer)

def rotate_270(face):
    transfer = [2, 5, 8, 1, 4, 7, 0, 3, 6]
    return rotate(face, transfer)
    
def maniplate(cube):
    cube['R'] = rotate(cube['R'])

notation = format_input()
cube = create()
"""
for direction in notation:
    print direction
    if len(direction) == 2:
        degree = direction[2]
        if degree == '2':
"""
print rotate_90([0,1,2,3,4,5,6,7,8])
            


