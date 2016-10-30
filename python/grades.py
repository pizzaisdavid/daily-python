import itertools

def main():
    numberOfGrades = 5
    raw = '38555555555'
    highest = 0
    indexCombinations = itertools.combinations(range(1, len(raw)), numberOfGrades - 1)
    
    for indices in indexCombinations:
        print('- {} -'.format(indices))
        grades = []
        for listPosition, index in enumerate(indices):
            previousIndexIndex = listPosition - 1
            previousIndex = 0
            if previousIndexIndex > 0:
                previousIndex = indices[previousIndexIndex]
            
            grades.append(raw[previousIndex:index])

        # don't forget the grade beween the last index and the end of the string.
        lastIndex = indices[-1]
        grades.append(raw[lastIndex:])
        
        grades = [int(g) for g in grades if g != '']

        print(grades)
        if len(grades) == numberOfGrades:
            average = sum(grades) / len(grades)
            if average > highest:
                highest = average
    print(highest)

if __name__ == '__main__':
    main()
