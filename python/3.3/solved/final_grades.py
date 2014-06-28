def grades(filename):
    raw_data = setup(filename)
    students = []
    for data in raw_data:
        students.append(Student(data))
    output(students)

def setup(filename):
    data = []
    file = open(filename)
    for line in file:
        first, comma, last, *assignments = line.split()
        if last == ',':
            last =''
        if assignments[0].isalpha():
            last += ' ' +  assignments.pop(0)
        if comma.isalpha():
            first += ' ' + comma
        data.append([first.strip(),
                     last.strip(),
                     sorted(map(int, assignments))
                     ])
    file.close()
    return data

class Student:
    def __init__(self, student):
        first, last, assignments = student
        self.first = first
        self.last = last
        self.assignments = assignments
        self.percent = Student.average(assignments)
        self.grade = Student.letter(self.percent)

    def average(grades):
        POINTS_POSSIBLE = 500
        CONVERT_TO_PERCENT = 100
        DECIMAL_PLACE = 2
        proportion = sum(grades) / POINTS_POSSIBLE
        grade = round(proportion, DECIMAL_PLACE) * CONVERT_TO_PERCENT
        return int(grade)
    
    def letter(percent):
        grade = {'A' : [100, 99, 98, 97, 96, 95, 94, 93],
                 'A-': [92, 91, 90],
                 'B+': [89, 88, 87],
                 'B' : [86, 85, 84, 83],
                 'B-': [82, 81, 80],
                 'C+': [79, 78, 77],
                 'C' : [76, 75, 74, 73],
                 'C-': [72, 71, 70],
                 'D+': [69, 68, 67],
                 'D' : [66, 65, 64, 63],
                 'D-': [62, 61, 60]
                 }
        for letter, percents in grade.items():
            if percent in percents:
                return letter
        if percent <= 59:
            return 'F'

def output(students):
    TEMPLATE = '{0}{1} {2}{3} {4}% ({5}){6}: {7}'
    length_first = longest(students, 'first')
    length_last = longest(students, 'last')
    print_header(length_first, length_last)
    students = reversed(sorted(students, key = lambda x: x.percent))
    for student in students:
        grade_space = grade_spacing(student.grade)
        first_spaces = spacing(length_first, student.first)
        last_spaces = spacing(length_last, student.last)
        print(TEMPLATE.format(student.first,
                              first_spaces,
                              student.last,
                              last_spaces,
                              student.percent,
                              student.grade,
                              grade_space,
                              ', '.join(map(str, student.assignments))
                              )
              )
                              
def longest(sequence, attribute):
    items = []
    for element in sequence:
        items.append(getattr(element, attribute))
    long = max(items, key=len)
    return len(long)

def print_header(length_first, length_last):
    HEADER = 'FIRST{0} LAST{1}   % ( ) :   ,   ,   ,   ,   '
    print(HEADER.format(spacing(length_first, 'FIRST'),
                        spacing(length_last, 'LAST')))
    print('-' * (length_first + length_last + 33))

def spacing(large, small):
    SPACE = ' '
    return (large - len(small)) * SPACE

def grade_spacing(grade):
    if grade in ['A', 'B', 'C', 'D', 'F']:
        return ' '
    return ''

grades('grades.txt')
